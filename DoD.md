# Definition of Done (DoD) — HopOn MVP

This document lists the objective acceptance criteria for the Minimum Viable Product (MVP) of HopOn. Each item is testable and must be satisfied before the project is considered done for the corresponding scope.

Core repository
- [ ] `README.md`, `DoD.md`, `BACKLOG.md`, and `HopOn.md` exist and explain the project and next steps.
- [ ] `IPClaim/` folder present with `stamp.sh`, `VERIFY.md` and `LICENSE-APC.md` (or `LICENSE-APC-VF.md`).
- [ ] `.github/workflows/timestamp.yml` exists in the repo root (for APC automated timestamping).

Authorship & proof
- [ ] The repository contains the IPClaim tooling (files above).
- [ ] After at least one commit, the author runs `./IPClaim/stamp.sh . "Author Name" apc` to apply the license and generate a timestamp proof. Verification steps must pass using `VERIFY.md`.

Functional MVP
- [ ] Matching Engine: A backend component implements a deterministic route-overlap matching function that returns matches only when the passenger destination lies along (or within an allowed deviation of) the driver’s declared route.
  - Acceptance: Unit tests that simulate driver route and passenger origin/destination verify the matching logic and pass in CI.
- [ ] Request Flow: End-to-end API flow where a passenger requests a ride and is assigned a driver (or receives a clear rejection) based on route alignment.
  - Acceptance: Integration test that creates a driver route and a passenger request; assertion that assignment occurs only when destination overlap condition is met.
- [ ] Pickup UX: System calculates and suggests a safe pickup point near the passenger (not in active traffic lanes) and displays a color code (driver/passenger) to identify each other.
  - Acceptance: Unit test for the pickup-suggestion component that filters out no-pick zones and prefers crosswalks/side-streets.
- [ ] Wait-time policy: Drivers are not required to wait more than 30 seconds for a passenger at a pickup point.
  - Acceptance: Simulation or test that enforces the 30s policy and reassigns drivers when timeouts occur.
- [ ] Deviation monitoring: Drivers who deviate beyond an allowed route tolerance are flagged and deviation events are recorded for enforcement.
  - Acceptance: Deviation detector unit tests and logging of events.

Pricing & Payments
- [ ] Pricing module exists and exposes a configurable baseline fare (example: per-10km value) and platform-cut percentage.
  - Acceptance: Unit tests confirm fare calculation for a set of sample trips.
- [ ] Payments integration stubbed or connected to a sandbox payment provider with documented flow (charging passengers, paying drivers, applying platform cut).

Safety & privacy
- [ ] Pickup suggestion enforces geofencing rules (no-pick zones) and recommends the safe side-of-street.
- [ ] Privacy policy and data retention notes are present in `docs/` and describe what location and telemetry data is retained and for how long.

Quality & operability
- [ ] Automated tests run on GitHub Actions and must pass on `main` branch (unit + critical integration tests).
- [ ] Linting, basic static checks, and a simple `make test` or `npm test` command are present.
- [ ] Basic telemetry: server logs include per-request identifiers enabling replay of matching decisions.

Documentation & handoff
- [ ] API specification (`docs/api.md`) exists with request/response examples for core endpoints (`/request_ride`, `/register_driver`, `/match`, `/report_deviation`).
- [ ] `BACKLOG.md` contains a prioritized, actionable list of tasks required to reach the DoD (this file).

Legal & IP
- [ ] IPClaim license/template files present for the author to stamp and publish.
- [ ] Short license and contributor guidance included (`IPClaim/README.md`).

Verification & acceptance
Each checkbox above must be accompanied by a one-line verification instruction (unit test name, integration script, or manual verification step). The item is considered complete only after that verification passes and is recorded in CI or in a PR review.
