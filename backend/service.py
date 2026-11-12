"""In-memory, single-process HopOn pilot engine.

Coordinates are latitude/longitude. The route supplied by a driver must follow
real streets: this prototype does not verify drivable roads or legal stopping.
"""
from __future__ import annotations

from math import cos, radians
from secrets import token_urlsafe
from threading import RLock
from time import time
from typing import Any

from backend.pricing import calculate_fare

EARTH_M = 6371000
MAX_WALK_M = 250
MAX_DROP_M = 100
PICKUP_ARRIVAL_M = 35
WAIT_SECONDS = 30
DRIVER_STALE_SECONDS = 300


def coordinate(value: Any) -> tuple[float, float]:
    if not isinstance(value, (list, tuple)) or len(value) != 2:
        raise ValueError("Expected [latitude, longitude]")
    try:
        from math import isfinite
        lat, lon = float(value[0]), float(value[1])
    except (TypeError, ValueError):
        raise ValueError("Invalid coordinates") from None
    if not (isfinite(lat) and isfinite(lon) and -90 <= lat <= 90 and -180 <= lon <= 180):
        raise ValueError("Coordinates out of range")
    return (lat, lon)


def distance_m(a: tuple[float, float], b: tuple[float, float]) -> float:
    from math import asin, sin, sqrt
    a1, o1, a2, o2 = map(radians, (*a, *b))
    dlat, dlon = a2 - a1, o2 - o1
    h = sin(dlat / 2) ** 2 + cos(a1) * cos(a2) * sin(dlon / 2) ** 2
    return 2 * EARTH_M * asin(min(1, sqrt(h)))


def projection(route: list[tuple[float, float]], point: tuple[float, float]):
    """(off-route distance, meters from route start, projected coordinate)."""
    if len(route) < 2:
        raise ValueError("Route needs at least two points")
    best = (float('inf'), 0.0, route[0])
    travelled = 0.0
    for a, b in zip(route, route[1:]):
        mid = radians((a[0] + b[0] + point[0]) / 3)
        scale_x = EARTH_M * cos(mid) * 3.141592653589793 / 180
        scale_y = EARTH_M * 3.141592653589793 / 180
        dx, dy = (b[1] - a[1]) * scale_x, (b[0] - a[0]) * scale_y
        seg_sq = dx * dx + dy * dy
        t = 0.0 if seg_sq == 0 else max(0.0, min(1.0, ((point[1] - a[1]) * scale_x * dx + (point[0] - a[0]) * scale_y * dy) / seg_sq))
        projected = (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t)
        off = distance_m(point, projected)
        seg_length = distance_m(a, b)
        if off < best[0]:
            best = (off, travelled + seg_length * t, projected)
        travelled += seg_length
    return best


def match_driver(driver: dict, origin, destination, excluded=(), now=None):
    if driver['id'] in excluded or not driver['online'] or driver['seats'] <= 0:
        return None
    if (time() if now is None else now) - driver['last_seen'] > DRIVER_STALE_SECONDS:
        return None
    route = driver['route']
    walk, pickup_progress, pickup = projection(route, origin)
    drop_offset, drop_progress, drop = projection(route, destination)
    _, driver_progress, _ = projection(route, driver['position'])
    if (walk > MAX_WALK_M or drop_offset > MAX_DROP_M or
            pickup_progress < driver_progress - 15 or drop_progress < pickup_progress + 150):
        return None
    remaining_km = (drop_progress - pickup_progress) / 1000
    fare = calculate_fare(remaining_km)
    return dict(driver_id=driver['id'], pickup=list(pickup), dropoff=list(drop),
                walk_m=round(walk), ride_km=round(remaining_km, 2),
                fare=fare, score=round(walk + max(0, pickup_progress - driver_progress) * .15, 2))


class HopOn:
    """Small local/demo engine; tokens isolate each session without accounts."""
    def __init__(self, clock=time):
        self.clock = clock
        self.lock = RLock()
        self.drivers: dict[str, dict] = {}
        self.rides: dict[str, dict] = {}

    def register_driver(self, payload: dict) -> dict:
        raw_route = payload.get('route')
        if not isinstance(raw_route, list) or not 2 <= len(raw_route) <= 100:
            raise ValueError('Driver route needs 2–100 waypoints')
        route = [coordinate(p) for p in raw_route]
        if sum(distance_m(a, b) for a, b in zip(route, route[1:])) < 150:
            raise ValueError('Driver route must be at least 150 meters long')
        position = coordinate(payload.get('position', route[0]))
        seats = int(payload.get('seats', 1))
        if not 1 <= seats <= 8:
            raise ValueError('Seats must be between 1 and 8')
        label = str(payload.get('label', 'Passing car')).strip()[:60] or 'Passing car'
        with self.lock:
            driver_id, token = token_urlsafe(12), token_urlsafe(32)
            self.drivers[driver_id] = dict(id=driver_id, token=token, route=route,
                position=position, seats=seats, label=label, online=True,
                last_seen=self.clock())
            return {'driver_id': driver_id, 'token': token, 'status': 'online'}

    def _driver(self, driver_id, token):
        driver = self.drivers.get(driver_id)
        if not driver or token != driver['token']:
            raise PermissionError('Driver session not found')
        return driver

    def update_driver(self, driver_id, token, payload: dict) -> dict:
        with self.lock:
            driver = self._driver(driver_id, token)
            if 'position' in payload:
                driver['position'] = coordinate(payload['position'])
            if 'online' in payload:
                driver['online'] = bool(payload['online'])
            driver['last_seen'] = self.clock()
            self._refresh()
            return {'status': 'online' if driver['online'] else 'offline'}

    def request_ride(self, payload: dict) -> dict:
        origin = coordinate(payload.get('origin'))
        destination = coordinate(payload.get('destination'))
        if distance_m(origin, destination) < 150:
            raise ValueError('Destination must be at least 150 meters away')
        with self.lock:
            ride_id, token = token_urlsafe(12), token_urlsafe(32)
            ride = dict(id=ride_id, token=token, origin=origin, destination=destination,
                status='searching', match=None, excluded=[], arrived_at=None,
                created_at=self.clock(), updated_at=self.clock())
            self.rides[ride_id] = ride
            self._refresh()
            return {'ride_id': ride_id, 'token': token, **self._public_ride(ride)}

    def _assign(self, ride):
        available = []
        for driver in self.drivers.values():
            active = sum(1 for r in self.rides.values() if r['id'] != ride['id'] and r['status'] in ('assigned', 'boarded') and r['match'] and r['match']['driver_id'] == driver['id'])
            if active >= driver['seats']:
                continue
            offer = match_driver(driver, ride['origin'], ride['destination'], ride['excluded'], self.clock())
            if offer:
                available.append(offer)
        if not available:
            return
        offer = min(available, key=lambda x: (x['score'], x['driver_id']))
        ride.update(status='assigned', match=offer, arrived_at=None,
                    updated_at=self.clock())

    def _refresh(self):
        now = self.clock()
        for ride in self.rides.values():
            if ride['status'] == 'assigned':
                driver = self.drivers.get(ride['match']['driver_id'])
                if not driver or not driver['online'] or now - driver['last_seen'] > DRIVER_STALE_SECONDS:
                    ride['excluded'].append(ride['match']['driver_id'])
                    ride.update(status='searching', match=None, arrived_at=None)
                    continue
                if distance_m(driver['position'], tuple(ride['match']['pickup'])) <= PICKUP_ARRIVAL_M:
                    if ride['arrived_at'] is None:
                        ride['arrived_at'] = now
                    elif now - ride['arrived_at'] > WAIT_SECONDS:
                        ride['excluded'].append(driver['id'])
                        ride.update(status='searching', match=None, arrived_at=None)
                else:
                    ride['arrived_at'] = None
        for ride in self.rides.values():
            if ride['status'] == 'searching':
                self._assign(ride)

    def _public_ride(self, ride):
        match = ride['match']
        driver = self.drivers.get(match['driver_id']) if match else None
        return {'id': ride['id'], 'status': ride['status'], 'match': match,
                'driver': ({'label': driver['label'], 'position': list(driver['position'])}
                           if driver else None),
                'origin': list(ride['origin']), 'destination': list(ride['destination']),
                'waiting_seconds': (max(0, WAIT_SECONDS - int(self.clock() - ride['arrived_at']))
                                    if ride['arrived_at'] is not None else None)}

    def get_ride(self, ride_id, token) -> dict:
        with self.lock:
            ride = self.rides.get(ride_id)
            if not ride or (token != ride['token'] and
               not (ride['match'] and (d := self.drivers.get(ride['match']['driver_id'])) and token == d['token'])):
                raise PermissionError('Ride session not found')
            self._refresh()
            return self._public_ride(ride)

    def driver_rides(self, driver_id, token) -> dict:
        with self.lock:
            driver = self._driver(driver_id, token)
            driver['last_seen'] = self.clock()
            self._refresh()
            assigned = [self._public_ride(r) for r in self.rides.values()
                        if r['match'] and r['match']['driver_id'] == driver_id
                        and r['status'] in ('assigned', 'boarded')]
            return {'driver': {'id': driver['id'], 'label': driver['label'],
                               'position': list(driver['position']), 'online': driver['online']},
                    'rides': assigned}

    def update_passenger(self, ride_id, token, payload):
        with self.lock:
            ride = self.rides.get(ride_id)
            if not ride or ride['token'] != token:
                raise PermissionError('Ride session not found')
            if ride['status'] == 'searching':
                ride['origin'] = coordinate(payload.get('origin'))
            self._refresh()
            return self._public_ride(ride)

    def action(self, ride_id, token, action):
        with self.lock:
            ride = self.rides.get(ride_id)
            if not ride:
                raise PermissionError('Ride not found')
            driver = self.drivers.get(ride['match']['driver_id']) if ride['match'] else None
            is_passenger = token == ride['token']
            is_driver = driver and token == driver['token']
            if not (is_passenger or is_driver):
                raise PermissionError('Ride session not found')
            if action == 'cancel' and ride['status'] in ('searching', 'assigned') and is_passenger:
                ride['status'] = 'cancelled'
            elif action == 'board' and ride['status'] == 'assigned' and is_passenger:
                if not driver or distance_m(driver['position'], tuple(ride['match']['pickup'])) > PICKUP_ARRIVAL_M:
                    raise ValueError('Driver has not reached the meeting point')
                ride['status'] = 'boarded'
            elif action == 'complete' and ride['status'] == 'boarded' and is_driver:
                ride['status'] = 'completed'
            else:
                raise ValueError('Action not available in current state')
            ride['updated_at'] = self.clock()
            return self._public_ride(ride)
