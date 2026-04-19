"""Deviation detection for drivers compared to declared route.

Provides a minimal detector that measures distance from current position to
the declared route and returns whether it exceeds a tolerance.
"""
from typing import List, Tuple
from backend.matching import min_distance_to_route

Coord = Tuple[float, float]


def has_deviated(route: List[Coord], location: Coord, tolerance_m: float = 50.0) -> bool:
    """Return True if `location` is further than `tolerance_m` from `route`."""
    d = min_distance_to_route(location, route)
    return d > float(tolerance_m)
