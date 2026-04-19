"""Matching engine utilities for HopOn MVP.

This module provides a deterministic, testable route-overlap check using
simple geographic math (haversine + equirectangular projection for local
point-to-segment distance). It intentionally avoids heavy GIS deps so tests
are portable in CI.
"""
from math import radians, cos, sin, asin, sqrt
from typing import List, Tuple

Coord = Tuple[float, float]  # (lat, lon)


def haversine(a: Coord, b: Coord) -> float:
    """Return distance between two (lat, lon) points in meters."""
    lat1, lon1 = a
    lat2, lon2 = b
    # convert decimal degrees to radians
    lat1, lon1, lat2, lon2 = map(radians, (lat1, lon1, lat2, lon2))
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    r = 6371000.0
    a_ = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a_))
    return r * c


def _latlon_to_xy(lat: float, lon: float, lat0: float) -> Tuple[float, float]:
    """Project lat/lon to local x,y using equirectangular approximation.

    lat0 is reference latitude (radians expected by caller conversion).
    Returns x,y in meters.
    """
    R = 6371000.0
    x = radians(lon) * cos(radians(lat0)) * R
    y = radians(lat) * R
    return x, y


def _point_segment_distance_m(point: Coord, a: Coord, b: Coord) -> float:
    """Distance from point to segment ab in meters (approximate).

    Uses equirectangular projection around the segment's latitude.
    """
    if a == b:
        return haversine(point, a)

    lat0 = (a[0] + b[0] + point[0]) / 3.0
    px, py = _latlon_to_xy(point[0], point[1], lat0)
    ax, ay = _latlon_to_xy(a[0], a[1], lat0)
    bx, by = _latlon_to_xy(b[0], b[1], lat0)

    vx = bx - ax
    vy = by - ay
    wx = px - ax
    wy = py - ay

    c1 = vx * wx + vy * wy
    if c1 <= 0:
        return sqrt((px - ax) ** 2 + (py - ay) ** 2)
    c2 = vx * vx + vy * vy
    if c2 <= c1:
        return sqrt((px - bx) ** 2 + (py - by) ** 2)
    t = c1 / c2
    projx = ax + t * vx
    projy = ay + t * vy
    return sqrt((px - projx) ** 2 + (py - projy) ** 2)


def min_distance_to_route(point: Coord, route: List[Coord]) -> float:
    """Return minimal distance in meters from point to polyline route."""
    if len(route) == 0:
        raise ValueError("Empty route")
    if len(route) == 1:
        return haversine(point, route[0])
    best = float("inf")
    for i in range(len(route) - 1):
        d = _point_segment_distance_m(point, route[i], route[i + 1])
        if d < best:
            best = d
    return best


def is_destination_on_route(route: List[Coord], dest: Coord, tolerance_m: float = 50.0) -> bool:
    """Return True if `dest` lies within `tolerance_m` meters of the route."""
    return min_distance_to_route(dest, route) <= float(tolerance_m)


def find_matching_drivers(drivers: List[dict], passenger_origin: Coord, passenger_dest: Coord, tolerance_m: float = 50.0) -> List[dict]:
    """Deterministic matching: return drivers whose routes include the passenger_dest within tolerance.

    Drivers should be an iterable of dicts containing at least `id` and `route` (list of coords).
    The result is deterministically ordered by driver `id`.
    """
    matches = []
    for drv in sorted(drivers, key=lambda d: str(d.get("id", ""))):
        route = drv.get("route", [])
        if not route:
            continue
        if is_destination_on_route(route, passenger_dest, tolerance_m=tolerance_m):
            matches.append(drv)
    return matches
