# HopOn

Instant walk-to-ride pickup platform — step out and get picked up by the next car whose route matches your destination.

Vision
- Make short, immediate, route-aligned rides the default urban micro-mobility option.
- Prioritize safety, minimal waiting (driver should not wait > 30s), and global applicability.

Core principles
- Route alignment: passengers are matched only when their destination lies along the driver’s route.
- Immediate pickup: the system favors the next available driver and optimizes pickup points.
- Safety-first pickup points: suggest safe boarding zones (crosswalks, side streets, designated hubs).
- Transparent, low pricing: configurable fares (example baseline discussed in design: 150–200 RSD per 10 km) and small platform cut (recommended 10–15%).
- Authorship proof: this repository includes the IPClaim toolkit to timestamp and assert authorship.

Repository contents
- `DoD.md` — Definition of Done with acceptance criteria.
- `BACKLOG.md` — Prioritized tasks to reach the DoD.


Quick start
1. Clone the repo:

```bash
git clone <your-repo-url> HopOn
cd HopOn
```

2. Inspect design and plans: open `HopOn.md`, `DoD.md`, `BACKLOG.md`.

Notes
- This repo is a product-design-first scaffold. The BACKLOG contains implementation epics for backend, mobile UI, safety, pricing, and operations.

Contributing
- Read `DoD.md` to understand acceptance criteria before implementing features.
- Use the `BACKLOG.md` to pick an epic and create a focused branch per task.

---
Created from `HopOn.md` design notes — see `HopOn.md` for the full conversation and design context.
