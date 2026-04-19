from backend import matching


def test_haversine_and_on_route():
    route = [(0.0, 0.0), (0.0, 0.1)]
    dest_on = (0.0, 0.05)
    dest_off = (0.01, 0.05)

    assert matching.is_destination_on_route(route, dest_on, tolerance_m=100)
    assert not matching.is_destination_on_route(route, dest_off, tolerance_m=100)


def test_find_matching_drivers():
    route = [(0.0, 0.0), (0.0, 0.1)]
    drivers = [{"id": "d1", "route": route}, {"id": "d2", "route": [(1.0, 1.0)]}]
    matches = matching.find_matching_drivers(drivers, (0.0, 0.02), (0.0, 0.05), tolerance_m=100)
    assert len(matches) == 1
    assert matches[0]["id"] == "d1"
