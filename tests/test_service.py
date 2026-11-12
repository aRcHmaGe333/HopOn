import pytest
from backend.service import HopOn, distance_m, projection

R = [[59.32, 18.05], [59.32, 18.06], [59.32, 18.075], [59.32, 18.09]]


def test_projection_metres_and_direction():
    offset, progress, where = projection(R, (59.32, 18.07))
    assert offset < 1
    assert 1000 < progress < 1500
    assert distance_m(tuple(where), (59.32, 18.07)) < 1


def test_full_ride_lifecycle_and_auth():
    now = [1000.0]
    engine = HopOn(clock=lambda: now[0])
    d = engine.register_driver({'route': R, 'position': R[0], 'label': 'My car'})
    p = engine.request_ride({'origin': [59.32, 18.065], 'destination': [59.32, 18.086]})
    assert p['status'] == 'assigned'
    assert p['match']['walk_m'] < 20
    assert p['match']['fare']['total'] > 0
    with pytest.raises(PermissionError):
        engine.get_ride(p['ride_id'], 'wrong')
    engine.update_driver(d['driver_id'], d['token'], {'position': p['match']['pickup']})
    ride = engine.get_ride(p['ride_id'], p['token'])
    assert ride['waiting_seconds'] == 30
    assert engine.action(p['ride_id'], p['token'], 'board')['status'] == 'boarded'
    assert engine.action(p['ride_id'], d['token'], 'complete')['status'] == 'completed'


def test_driver_direction_and_distance():
    e = HopOn()
    e.register_driver({'route': R, 'position': [59.32, 18.08]})
    r = e.request_ride({'origin': [59.32, 18.058], 'destination': [59.32, 18.086]})
    assert r['status'] == 'searching'
    with pytest.raises(ValueError):
        e.register_driver({'route': [[1000, 0], [59.3, 18.0]]})
    r2 = e.request_ride({'origin': [59.4, 18.058], 'destination': [59.32, 18.086]})
    assert r2['status'] == 'searching'


def test_wait_then_reassign():
    now = [100.0]
    e = HopOn(clock=lambda: now[0])
    d1 = e.register_driver({'route': R, 'position': R[0]})
    d2 = e.register_driver({'route': R, 'position': R[0]})
    p = e.request_ride({'origin': [59.32, 18.065], 'destination': [59.32, 18.086]})
    first = p['match']['driver_id']
    ds = {d1['driver_id']: d1, d2['driver_id']: d2}
    e.update_driver(first, ds[first]['token'], {'position': p['match']['pickup']})
    now[0] += 31
    actual = e.get_ride(p['ride_id'], p['token'])
    assert actual['status'] == 'assigned'
    assert actual['match']['driver_id'] != first


def test_bad_coords_and_cancel():
    e = HopOn()
    with pytest.raises(ValueError):
        e.request_ride({'origin': [91, 18], 'destination': [59, 18]})
    p = e.request_ride({'origin': [59.32, 18.065], 'destination': [59.32, 18.086]})
    assert e.action(p['ride_id'], p['token'], 'cancel')['status'] == 'cancelled'


def test_seat_reserved_and_released():
    now = [1000.0]
    e = HopOn(clock=lambda: now[0])
    e.register_driver({'route': R, 'seats': 1})
    a = e.request_ride({'origin': [59.32, 18.065], 'destination': [59.32, 18.086]})
    b = e.request_ride({'origin': [59.32, 18.066], 'destination': [59.32, 18.087]})
    assert a['status'] == 'assigned' and b['status'] == 'searching'
    e.action(a['ride_id'], a['token'], 'cancel')
    assert e.get_ride(b['ride_id'], b['token'])['status'] == 'assigned'


def test_driver_declines_then_other_driver_is_used():
    now = [1000.0]
    e = HopOn(clock=lambda: now[0])
    d1 = e.register_driver({'route': R})
    d2 = e.register_driver({'route': R})
    a = e.request_ride({'origin': [59.32, 18.065], 'destination': [59.32, 18.086]})
    first = a['match']['driver_id']
    token = next(d['token'] for d in [d1, d2] if d['driver_id'] == first)
    r = e.action(a['ride_id'], token, 'decline')
    assert r['match']['driver_id'] != first


def test_walking_live_update():
    e = HopOn()
    e.register_driver({'route': R})
    a = e.request_ride({'origin': [59.321, 18.065], 'destination': [59.32, 18.086]})
    initial = a['match']['walk_m']
    r = e.update_passenger(a['ride_id'], a['token'], {'origin': [59.32, 18.065]})
    assert r['match']['walk_m'] < initial
