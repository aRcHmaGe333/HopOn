"""Pricing module for HopOn MVP.

Simple baseline fare calculation per distance with platform cut.
"""
from typing import Dict


def calculate_fare(distance_km: float, baseline_per_10km: float = 150.0, platform_cut: float = 0.10) -> Dict[str, float]:
    """Calculate fare given distance in km.

    Returns a dict with `total`, `driver_amount`, and `platform_cut`.
    """
    if distance_km < 0:
        raise ValueError("distance_km must be non-negative")
    multiplier = distance_km / 10.0
    total = baseline_per_10km * multiplier
    cut = round(total * float(platform_cut), 2)
    driver_amount = round(total - cut, 2)
    return {"total": round(total, 2), "driver_amount": driver_amount, "platform_cut": cut}
