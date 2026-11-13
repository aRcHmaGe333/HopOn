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

## Run the software

**Windows:** Clone or download the repository, then double-click `start_hopon.cmd`. Python 3.10+ is required. No extra Python packages are required to run the pilot.

**Any platform:**

```bash
python hopon_app.py
```

Open **http://127.0.0.1:8787** in two browser tabs: Driver → Example driver → Go online; Passenger → Example trip → Find a passing ride. The screens communicate through the same local service. Use **Simulate arrival** on the driver side, then board and complete the trip.

The new local pilot supports multiple cars and passengers, ordered route matching, seat reservations, live GPS updates when opted in, route-based example fares, driver decline, and automatic reassignment after a 30-second pickup wait. Source: [local pilot server](hopon_app.py) · [mobile-friendly passenger/driver interface](web/index.html) · [tests](tests/).

The GitHub Pages [browser simulator](https://archmage333.github.io/HopOn/) is a separate **static demonstration**, not the server-backed passenger/driver application.

**Current boundary:** This is runnable prototype software, not a transport service. The route points are provided by the driver; pickup suggestions have not been validated against actual road rules or stopping restrictions. There is no production hosting, persistent database, verified identity, insurance integration, or real payment processing. Pilot sessions live in memory and disappear when the server stops. Use test data. Never expose the local HTTP server directly to the public internet.

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

Current stage: **algorithmic MVP + working two-sided local pilot + separate static simulator**.

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

## Better implementations

The purpose of this project matters more than its current design. Its architecture and methods are examples of how to achieve that purpose, not permanent limits. A better approach can replace any part or all of the implementation when it produces a better result. Document new methods as they are developed; preserve the original publication history.

[Principle shared by all projects](https://github.com/aRcHmaGe333/aRcHmaGe333/blob/main/UNIVERSAL_IMPLEMENTATION_PRINCIPLES.md)
