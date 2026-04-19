from backend.deviation import has_deviated


def test_deviation_detector():
    route = [(0.0, 0.0), (0.0, 0.1)]
    on_route = (0.0, 0.05)
    off_route = (0.01, 0.05)
    assert not has_deviated(route, on_route, tolerance_m=100)
    assert has_deviated(route, off_route, tolerance_m=500)
