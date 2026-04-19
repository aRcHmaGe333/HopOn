from backend import pricing


def test_pricing_baseline():
    res = pricing.calculate_fare(12.5, baseline_per_10km=150.0, platform_cut=0.10)
    assert res["total"] == 187.5
    assert res["platform_cut"] == 18.75
    assert res["driver_amount"] == 168.75
