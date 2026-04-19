# BACKLOG — HopOn MVP

This backlog organizes work into epics and prioritized tasks to reach the DoD. Pick a single issue from the top of the list per branch.

Epic: Repository & foundation (P0)
- [ ] Initialize repository scaffold and CI (this commit).
- [ ] Add `DoD.md`, `BACKLOG.md`, `README.md` (done).
- [ ] Add IPClaim toolkit into `IPClaim/` and include `stamp.sh`, `VERIFY.md`, license templates. (P0)
- [ ] Add `.github/workflows/timestamp.yml` at repo root. (P0)

Epic: Core backend (P0 → P1)
- [ ] Create backend project skeleton (`/backend`) with chosen stack (Node/Express, Python/Flask, or similar). (P0)
- [ ] Auth & profiles: endpoints for driver/passenger registration, basic verification stub. (P0)
- [ ] Matching service: implement deterministic route-overlap function + unit tests. (P0)
- [ ] Request flow endpoints: `/request_ride`, `/register_driver`, `/match`. (P0)
- [ ] Deviation detection service + logging. (P1)

Epic: Mapping & GPS (P0 → P1)
- [ ] Integrate map provider SDK (Mapbox / Google Maps / OpenStreetMap) with routing. (P0)
- [ ] Implement safe-pickup-point algorithm (geofence/no-pick filtering). (P0)
- [ ] Server-side simulator to validate pick-up suggestions for unit tests. (P1)

Epic: Passenger & Driver apps (P1)
- [ ] Minimal passenger web UI to request ride and show assigned driver on map. (P1)
- [ ] Minimal driver web UI to declare route, accept pickups, and display color code. (P1)
- [ ] Color-code protocol: generate short visual code and brief handshake flow. (P1)

Epic: Pricing & payments (P1)
- [ ] Pricing module: implement baseline fare calculation per distance and platform cut parameter. (P1)
- [ ] Integrate payment provider sandbox (Stripe / Adyen / local). (P1)

Epic: Safety, moderation & compliance (P1 → P2)
- [ ] Rules engine for deviations, warnings, and automated bans. (P1)
- [ ] Privacy & data retention policy draft. (P1)
- [ ] Driver vetting process (documented). (P2)

Epic: Testing & CI (P0 → P1)
- [ ] Unit tests for matching, pickup suggestion, pricing. (P0)
- [ ] Integration test that simulates a full match lifecycle. (P0)
- [ ] Add linters and `make test` or `npm test`. (P0)

Epic: DevOps & release (P2)
- [ ] Containerize backend (Dockerfile) and provide local run scripts. (P2)
- [ ] Add deployment/infra notes (`deploy/README.md`). (P2)

Epic: Docs & outreach (P2)
- [ ] API spec `docs/api.md` and developer onboarding `docs/dev-setup.md`. (P2)
- [ ] Short elevator pitch and one-paragraph description for accelerator submission (non-confidential variant). (P0)

Epic: Legal & IP (P0)
- [ ] Apply IPClaim stamp and commit timestamp proof after first commit. (P0)
- [ ] If author wants profit sharing, choose `apc-vf` license and populate pricing table in `LICENSE-APC-VF.md`. (P1)

Notes and estimates
- Label tasks with `P0` (highest-priority) for items required to validate the concept and satisfy the DoD checklist. Break tasks into smaller GitHub issues when implementing.
