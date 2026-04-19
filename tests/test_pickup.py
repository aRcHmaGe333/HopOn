from backend import pickup


def test_pickup_avoids_no_pick_zone():
    passenger = (0.0, 0.0)
    # place a no-pick zone directly north of passenger at ~10m
    zone = {"center": (0.00009, 0.0), "radius_m": 20}
    suggestion = pickup.suggest_pickup(passenger, [zone], max_radius_m=50)
    assert suggestion is not None
    # ensure suggestion is not inside the no-pick zone
    assert pickup._distance_m(suggestion, zone["center"]) > zone["radius_m"]
