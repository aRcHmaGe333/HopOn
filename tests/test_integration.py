from backend import matching, pricing


def test_request_flow_assigns_driver():
    # Driver declares a route that passes near destination
    driver = {"id": "d1", "route": [(0.0, 0.0), (0.0, 0.1)]}
    drivers = [driver]

    passenger_origin = (0.0, 0.02)
    passenger_dest = (0.0, 0.05)

    matches = matching.find_matching_drivers(drivers, passenger_origin, passenger_dest, tolerance_m=100)
    assert len(matches) == 1
    assert matches[0]["id"] == "d1"

    # pricing sanity check
    fare = pricing.calculate_fare(5.0)
    assert fare["total"] >= 0
