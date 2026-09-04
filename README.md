# HopOn

Cars keep moving around with empty seats. People keep standing around trying to get somewhere. A lot of the time those two routes already overlap.

HopOn is basically: **walk to the next sensible pickup point and get into a car that was already going your way anyway.**

No dedicated driver has to come find you. No five-minute curbside ritual. No "your driver is completing another trip" opera. The route overlap is the whole point.

## How it works

A driver declares where they are going.

A passenger asks to go somewhere nearby.

HopOn only matches them when the passenger can be picked up safely and the destination sits on, or close enough to, the driver's existing route.

The passenger walks to the pickup point. The driver should not be sitting there waiting for ages, so the system enforces a short dwell window and reassigns if it falls apart.

The current design also includes a simple visual handshake so the right person finds the right car without doing license-plate archaeology in traffic.

## What actually exists

This is not just a sketch anymore. The repo has working Python modules for:

- route-overlap matching
- safe pickup-point selection
- no-pick geofences
- route-deviation detection
- 30-second waiting/reassignment logic
- distance-based pricing
- payment sandboxing
- telemetry/audit logging
- tests

There is also a live browser simulator:

**https://archmage333.github.io/HopOn/**

Current stage: **algorithmic MVP + live simulator**.

## Why I care about this

Because ride-hailing usually creates another trip to solve a trip.

HopOn is trying to use a trip that already exists.

That is better economically if the matching works, and it is obviously interesting environmentally because an occupied seat is doing more useful work than an empty one.

The useful question now is not whether shared rides are a known concept. They are. The question is whether immediate route-aligned pickup can be made easy enough that normal people actually use it without turning the driver's existing trip into a punishment.

That is what this prototype is for.

## What needs to happen next

The next real step is a bounded field test, not another year of drawing arrows.

That means:

1. pick one dense corridor
2. build the lightweight mobile client around the working matching logic
3. sort out safety, insurance, local rules and payment handling
4. seed enough drivers/passengers that the test is not fake
5. measure waiting, walking, detour, occupancy and repeat use

If it survives that, then we have something worth scaling.

## Run it

```bash
git clone https://github.com/aRcHmaGe333/HopOn.git
cd HopOn
python -m pytest -q
```

Windows PowerShell:

```powershell
.\run_tests.ps1
```

## Useful repo material

- [Live simulator](https://archmage333.github.io/HopOn/)
- [Investment / funding one-pager](docs/INVESTOR_ONE_PAGER.md)
- [Funding targets](docs/FUNDING_TARGETS.md)
- [Backlog](BACKLOG.md)
- [Definition of Done](DoD.md)

## IP / verification

The project is published under the **IPClaim APC License v1.1** with RFC 3161 timestamping.

- [LICENSE.md](LICENSE.md)
- [VERIFY.md](VERIFY.md)

The timestamps are there so authorship can be checked independently instead of being a "trust me bro" paragraph.

---

If you fund mobility, run transport systems, work with cities, build insurance/regulatory sandboxes, or can help get one real corridor tested properly, I want to talk.
