"""Driver wait-time policy utilities.

Simple functions to determine when drivers exceed allowed wait times and should
be re-assigned.
"""
from typing import List, Dict


def timed_out_assignments(assignments: List[Dict], now_ts: float, timeout_s: int = 30) -> List[Dict]:
    """Return list of assignment dicts whose `assigned_at` timestamp is older than timeout.

    Each assignment is expected to contain `driver_id` and `assigned_at` (unix seconds).
    """
    timed_out = []
    for a in assignments:
        assigned_at = float(a.get("assigned_at", 0))
        if (now_ts - assigned_at) > timeout_s:
            timed_out.append(a)
    return timed_out
