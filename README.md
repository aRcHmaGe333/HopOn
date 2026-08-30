# HopOn

Instant walk-to-ride pickup platform — step out and get picked up by the next car whose route matches your destination.

## Vision
- Make short, immediate, route-aligned rides the default urban micro-mobility option.
- Prioritize passenger safety, minimal driver waiting (driver should not wait > 30s), and algorithmic route overlap.

## Core Principles
- **Route alignment**: passengers are matched only when their destination lies along (or within allowed deviation of) the driver’s declared route.
- **Immediate pickup**: favors the next available driver and optimizes pickup boarding zones.
- **Safety-first pickup points**: suggests safe boarding zones (crosswalks, side streets, designated hubs) avoiding active traffic lanes.
- **Transparent, predictable pricing**: configurable baseline fare per distance and platform cut.
- **Authorship proof**: published under the **IPClaim APC License** with automated, independently verifiable RFC 3161 cryptographic timestamping.

## Repository Contents
- `LICENSE.md` — Author declaration (**Slavko Stojnić**) and All Rights Reserved IP claim under APC v1.1.
- `VERIFY.md` — Step-by-step instructions to verify the RFC 3161 cryptographic timestamp using OpenSSL.
- `backend/` — Core algorithmic Python MVP modules:
  - `matching.py`: Deterministic route-overlap calculations (haversine + segment projections).
  - `pickup.py`: Safe pickup point suggester with geofence no-pick filtering.
  - `deviation.py`: Real-time driver deviation detection against declared route.
  - `waiting.py`: 30-second driver timeout enforcement and reassignment logic.
  - `pricing.py`: Distance-based fare calculation with configurable platform cut.
  - `payments.py`: Payment provider sandbox harness.
  - `telemetry.py`: Request-scoped logging and audit trails.
- `tests/` — Full test suite verifying core functional algorithms and integrations.
- `docs/` — Public specifications, privacy documentation, and web showcase.
- `DoD.md` — Definition of Done with verifiable acceptance criteria.
- `BACKLOG.md` — Prioritized roadmap of next steps.
- `HopOn.md` — Invention ideation and design notes.

## IPClaim & Verification
This repository is published as a **public, timestamped, cryptographically verifiable authorship and IP claim record**.

- **Author**: Slavko Stojnić
- **License**: [IPClaim APC License v1.1](LICENSE.md)
- **Verification Guide**: [VERIFY.md](VERIFY.md)
- **Automated Timestamping**: On push to `main`, GitHub Actions queries an RFC 3161 Time Stamping Authority (FreeTSA.org) and commits the signed `.tsr` token into `.timestamps/`. Anyone can verify the repository state independently using standard OpenSSL tools.

## Quick Start & Testing

1. Clone the repo:
```bash
git clone https://github.com/aRcHmaGe333/HopOn.git
cd HopOn
```

2. Run the automated test suite:
```bash
python -m pytest -q
```
or on Windows PowerShell:
```powershell
.\run_tests.ps1
```

---
**Authorship & Patent Claim established by public record.**  
Verified by cryptography. Maintained by the internet. Gatekept by no one.

