import time
from backend.waiting import timed_out_assignments


def test_timed_out_assignments():
    now = 1000.0
    assignments = [
        {"driver_id": "d1", "assigned_at": now - 5},
        {"driver_id": "d2", "assigned_at": now - 40},
    ]
    timed_out = timed_out_assignments(assignments, now, timeout_s=30)
    assert len(timed_out) == 1
    assert timed_out[0]["driver_id"] == "d2"
