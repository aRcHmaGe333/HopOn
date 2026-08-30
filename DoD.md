# Definition of Done (DoD) — HopOn MVP

This document lists the objective acceptance criteria for the Minimum Viable Product (MVP) of HopOn. Each item is testable and must be satisfied before the project is considered done for the corresponding scope.

Core repository
- [x] `README.md`, `DoD.md`, `BACKLOG.md`, and `HopOn.md` exist and explain the project and next steps.
- [x] `IPClaim/` folder present with `stamp.sh`, `VERIFY.md` and `LICENSE-APC.md` (or `LICENSE-APC-VF.md`).
- [x] `.github/workflows/timestamp.yml` exists in the repo root (for APC automated timestamping).

Authorship & proof
- [x] The repository contains the IPClaim tooling (files above).
- [x] Repository includes root `LICENSE.md` and `VERIFY.md` asserting authorship and automated RFC 3161 timestamping workflow.

Functional MVP
- [x] Matching Engine: A backend component implements a deterministic route-overlap matching function that returns matches only when the passenger destination lies along (or within an allowed deviation of) the driver’s declared route.
  - Acceptance: Unit tests that simulate driver route and passenger origin/destination verify the matching logic and pass in CI (`tests/test_matching.py`, `tests/test_integration.py`).
- [x] Request Flow: End-to-end API flow where a passenger requests a ride and is assigned a driver (or receives a clear rejection) based on route alignment.
  - Acceptance: Integration test that creates a driver route and a passenger request; assertion that assignment occurs only when destination overlap condition is met (`tests/test_integration.py`).
- [x] Pickup UX: System calculates and suggests a safe pickup point near the passenger (not in active traffic lanes) and displays a color code (driver/passenger) to identify each other.
  - Acceptance: Unit test for the pickup-suggestion component that filters out no-pick zones and prefers crosswalks/side-streets (`tests/test_pickup.py`).
- [x] Wait-time policy: Drivers are not required to wait more than 30 seconds for a passenger at a pickup point.
  - Acceptance: Simulation or test that enforces the 30s policy and reassigns drivers when timeouts occur (`tests/test_waiting.py`).
- [x] Deviation monitoring: Drivers who deviate beyond an allowed route tolerance are flagged and deviation events are recorded for enforcement.
  - Acceptance: Deviation detector unit tests and logging of events (`tests/test_deviation.py`).

Pricing & Payments
- [x] Pricing module exists and exposes a configurable baseline fare (example: per-10km value) and platform-cut percentage.
  - Acceptance: Unit tests confirm fare calculation for a set of sample trips (`tests/test_pricing.py`).
- [x] Payments integration stubbed or connected to a sandbox payment provider with documented flow (charging passengers, paying drivers, applying platform cut) (`tests/test_payments.py`).

Safety & privacy
- [x] Pickup suggestion enforces geofencing rules (no-pick zones) and recommends the safe side-of-street.
- [x] Privacy policy and data retention notes are present in `docs/` and describe what location and telemetry data is retained and for how long.

Quality & operability
- [x] Automated tests run on GitHub Actions and must pass on `main` branch (unit + critical integration tests).
- [x] Linting, basic static checks, and a simple `make test` or `npm test` command are present.
- [x] Basic telemetry: server logs include per-request identifiers enabling replay of matching decisions.

Documentation & handoff
- [x] API specification (`docs/api.md`) exists with request/response examples for core endpoints (`/request_ride`, `/register_driver`, `/match`, `/report_deviation`).
- [x] `BACKLOG.md` contains a prioritized, actionable list of tasks required to reach the DoD (this file).

Legal & IP
- [x] IPClaim license/template files present for the author to stamp and publish.
- [x] Short license and contributor guidance included (`IPClaim/README.md`, `LICENSE.md`, `VERIFY.md`).

Verification & acceptance
Each checkbox above must be accompanied by a one-line verification instruction (unit test name, integration script, or manual verification step). The item is considered complete only after that verification passes and is recorded in CI or in a PR review.
