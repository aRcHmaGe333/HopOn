"""Pickup suggestion utilities.

This module provides a tiny, testable pickup point suggester that avoids
no-pick zones and prefers nearby safe offsets. It is intentionally simple
so unit tests and CI remain lightweight.
"""
from typing import List, Tuple, Optional
from math import sqrt

Coord = Tuple[float, float]


def _deg_offset_for_meters(meters: float) -> float:
    """Approximate degree delta for ~meters (latitude-based)."""
    return meters / 111000.0


def _distance_m(a: Coord, b: Coord) -> float:
    # small-distance euclidean approx using degrees -> meters
    lat_deg = (a[0] - b[0]) * 111000.0
    lon_deg = (a[1] - b[1]) * 111000.0
    return sqrt(lat_deg * lat_deg + lon_deg * lon_deg)


def suggest_pickup(passenger_location: Coord,
                   no_pick_zones: List[dict],
                   max_radius_m: float = 50.0) -> Optional[Coord]:
    """Return a nearby safe pickup coordinate or None if none found.

    `no_pick_zones` is a list of dicts with `center`:(lat,lon) and `radius_m`.
    The suggester generates a small set of candidate offsets and returns the
    nearest one that does not fall inside any no-pick zone.
    """
    lat, lon = passenger_location
    # Candidate offsets (meters)
    offsets = [
        (0, 0),
        (10, 0),
        (-10, 0),
        (0, 10),
        (0, -10),
        (15, 15),
        (-15, -15),
    ]

    candidates = []
    for dy, dx in offsets:
        dlat = _deg_offset_for_meters(dy)
        dlon = _deg_offset_for_meters(dx)
        candidates.append((lat + dlat, lon + dlon))

    def inside_no_pick(pt: Coord) -> bool:
        for z in no_pick_zones:
            center = z.get("center")
            r = float(z.get("radius_m", 0))
            if _distance_m(pt, center) <= r:
                return True
        return False

    safe = [c for c in candidates if not inside_no_pick(c)]
    if not safe:
        return None
    # return nearest candidate to passenger
    safe_sorted = sorted(safe, key=lambda p: _distance_m(p, passenger_location))
    return safe_sorted[0]
