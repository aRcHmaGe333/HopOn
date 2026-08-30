# API — HopOn (MVP)

This document lists the core endpoints and request/response examples for the HopOn MVP.

Core endpoints (intended surface; the current codebase implements the core matching logic used by these endpoints):

- `POST /register_driver`
  - Body: `{ "id": "driver-id", "route": [[lat, lon], [lat, lon], ...] }`
  - Response: `200 OK` on success

- `POST /request_ride`
  - Body: `{ "passenger_id": "p1", "origin": [lat, lon], "destination": [lat, lon] }`
  - Response: `200 OK` with assignment `{ "assigned_driver": "d1" }` or `{ "assigned_driver": null, "reason": "no_match" }`

- `POST /match` (internal/test endpoint)
  - Body: `{ "drivers": [...], "origin": [...], "destination": [...] }`
  - Response: list of matching drivers based on deterministic route-overlap logic.

Note: The repository currently contains the deterministic matching implementation under `backend/matching.py` and unit/integration tests in `tests/` to validate the logic. The HTTP endpoints are intentionally left as a thin wrapper to allow API technology choice (Flask/FastAPI/Express) during implementation.
