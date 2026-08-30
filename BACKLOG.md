# BACKLOG — HopOn MVP

This backlog organizes work into epics and prioritized tasks to reach the DoD. Pick a single issue from the top of the list per branch.

Epic: Repository & foundation (P0)
- [x] Initialize repository scaffold and CI. (P0)
- [x] Add `DoD.md`, `BACKLOG.md`, `README.md`. (P0)
- [x] Add IPClaim toolkit into `IPClaim/` and include `stamp.sh`, `VERIFY.md`, license templates. (P0)
- [x] Add `.github/workflows/timestamp.yml` at repo root. (P0)
- [x] Add root `LICENSE.md` and `VERIFY.md` with explicit authorship and verification guides. (P0)

Epic: Core backend (P0 → P1)
- [x] Create backend project skeleton (`/backend`) with lightweight modular Python components. (P0)
- [ ] Auth & profiles: endpoints for driver/passenger registration, basic verification stub. (P0)
- [x] Matching service: implement deterministic route-overlap function + unit tests. (P0)
- [ ] Request flow endpoints: `/request_ride`, `/register_driver`, `/match` HTTP service wrapper. (P0)
- [x] Deviation detection service + logging. (P1)

Epic: Mapping & GPS (P0 → P1)
- [ ] Integrate map provider SDK (Mapbox / Google Maps / OpenStreetMap) with routing. (P0)
- [x] Implement safe-pickup-point algorithm (geofence/no-pick filtering). (P0)
- [x] Server-side simulator / tests to validate pick-up suggestions for unit tests. (P1)

Epic: Passenger & Driver apps (P1)
- [ ] Minimal passenger web UI to request ride and show assigned driver on map. (P1)
- [ ] Minimal driver web UI to declare route, accept pickups, and display color code. (P1)
- [ ] Color-code protocol: generate short visual code and brief handshake flow. (P1)

Epic: Pricing & payments (P1)
- [x] Pricing module: implement baseline fare calculation per distance and platform cut parameter. (P1)
- [x] Integrate payment provider sandbox stub (in-memory charge/payout test harness). (P1)

Epic: Safety, moderation & compliance (P1 → P2)
- [x] Rules engine for deviations, warnings, and automated timeouts (30s wait policy). (P1)
- [x] Privacy & data retention policy draft (`docs/privacy.md`). (P1)
- [ ] Driver vetting process (documented). (P2)

Epic: Testing & CI (P0 → P1)
- [x] Unit tests for matching, pickup suggestion, pricing, deviation, waiting policy. (P0)
- [x] Integration test that simulates a full match lifecycle. (P0)
- [x] Add Makefile test targets and GitHub Actions CI workflow (`ci.yml`). (P0)

Epic: DevOps & release (P2)
- [ ] Containerize backend (Dockerfile) and provide local run scripts. (P2)
- [ ] Add deployment/infra notes (`deploy/README.md`). (P2)

Epic: Docs & outreach (P2)
- [x] API spec `docs/api.md` and developer onboarding guidelines. (P2)
- [x] Elevator pitch, landing page, and one-paragraph description (`docs/index.html`, `README.md`). (P0)

Epic: Legal & IP (P0)
- [x] Establish root IPClaim / APC license (`LICENSE.md`) declaring authorship (`Slavko Stojnić`). (P0)
- [x] Configure automated RFC 3161 cryptographic timestamping workflow (`timestamp.yml`). (P0)
- [x] Independent verification guide (`VERIFY.md`). (P0)
- [ ] If author wants profit sharing, choose `apc-vf` license and populate pricing table in `LICENSE-APC-VF.md`. (P1)

Notes and estimates
- Label tasks with `P0` (highest-priority) for items required to validate the concept and satisfy the DoD checklist. Break tasks into smaller GitHub issues when implementing.
