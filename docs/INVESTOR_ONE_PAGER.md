# HopOn — Executive One-Pager & Investment Thesis

> **Vision**: Transform urban micro-mobility by turning everyday commuter cars into an instant, zero-detour transit mesh.

---

## 1. Executive Summary
HopOn is an instant walk-to-ride platform connecting walking pedestrians with private drivers who are *already* traveling along the exact same corridor. Unlike traditional ride-hailing (Uber/Lyft) which summons dedicated drivers and induces detours, or long-distance carpooling (BlaBlaCar) which requires advance booking, HopOn operates in real-time with **zero driver detour**, **safe pedestrian pickup zones**, and a **maximum 30-second curb dwell time**.

- **Core Innovation**: Deterministic route-overlap matching, dynamic walk-to-ride pickup routing, and visual color-code handshakes.
- **Economic Model**: 50–70% cheaper than taxis; drivers offset fuel and operating costs on existing commutes; 10–15% platform take.
- **Defensibility**: Independently verifiable authorship and architecture established under the **IPClaim APC License v1.1** with RFC 3161 cryptographic timestamps.

---

## 2. The Problem
1. **Pervasive Vehicle Inefficiency**: Average private vehicle occupancy globally remains stagnant at **~1.5 passengers**, with billions of empty seats moving daily along high-density commuter corridors.
2. **Ride-Hailing Inflation & Congestion**: Traditional ride-hailing adds deadhead miles (drivers cruising without passengers) and imposes steep surge pricing (– for short urban trips).
3. **Public Transit Gaps**: Fixed-route buses and trams suffer from rigid scheduling, crowding, and the "first/last mile" friction, forcing urban commuters to default to solo driving.

---

## 3. The Solution & Mechanics

| Feature | HopOn Architecture | Traditional Ride-Hailing |
|---|---|---|
| **Driver Path** | Strict adherence to existing route (tolerance < 50m) | Forced detours to passenger doorsteps |
| **Pickup Location** | Walk-to-ride safe curb offsets (crosswalks, side streets) | Unpredictable doorstops, double-parking |
| **Boarding Dwell Time** | **< 30 seconds** (enforced via timeout & reassignment) | 3–10 minutes waiting at curb |
| **Identification** | Synchronized dynamic color-code screen handshake | License plate hunting in active traffic |
| **Pricing** | Predictable baseline (.50–.50 per 10km) | High base fare + dynamic surge multipliers |

---

## 4. Market Opportunity & Impact
- **Total Addressable Market (TAM)**: Global urban mobility and shared transit market exceeds **+**.
- **Serviceable Addressable Market (SAM)**: Daily urban commuter trips under 15km in dense metropolitan centers.
- **Sustainability / ESG**: Eliminates redundant vehicle trips. Shifting 15% of solo commuters to corridor carpooling reduces urban transport emissions by up to 25% without adding new municipal fleet infrastructure.

---

## 5. Unit Economics & Monetization
- **Baseline Fare**: Estimated at ~.50 – .50 per 10km.
- **Driver Split**: 85–90% credited to driver (instantly covering fuel, wear, and parking costs for trips they were already making).
- **Platform Fee**: 10–15% frictionless cut per transaction.
- **Customer Acquisition**: Low CAC due to symbiotic viral loops—passengers become drivers, and drivers invite colleagues along commuter corridors.

---

## 6. Intellectual Property & Defensibility
- **Authorship & Provenance**: Disclosed and sealed under **IPClaim APC License v1.1** by inventor **Slavko Stojnić**.
- **Cryptographic Evidence**: Merkle tree proofs anchored via independent RFC 3161 Time Stamping Authorities (FreeTSA) on GitHub public infrastructure.
- **Verification**: Verifiable by any auditor or institutional diligence partner using standard OpenSSL tooling (see [VERIFY.md](../VERIFY.md)).

---

## 7. Milestone-Based Execution Sequencing

- **Sequence 1: IP Lockdown & Algorithmic MVP** *(Completed)*
  - Sealed core routing, deviation, and pricing algorithms with passing test suites.
  - Published public repository and verified RFC 3161 timestamp proof.
- **Sequence 2: Institutional Outreach & Interactive Simulation** *(Current)*
  - Live interactive web simulator deployed on GitHub Pages.
  - Institutional grant and accelerator applications (EIT Urban Mobility, Horizon Europe, Climate Accelerators).
  - Co-founder and lead engineer talent search.
- **Sequence 3: Lightweight Mobile Client & Municipal Sandbox Pilot**
  - Cross-platform mobile MVP (passenger request + driver route declaration).
  - Bounded geofenced pilot along a single high-frequency commuter corridor (e.g. university campus to transit terminal).
- **Sequence 4: Commercial Launch & City Partner Expansion**
  - Integrate production payment gateways (Stripe/local rail).
  - Scale corridor density and transit authority integration.

---

## 8. The Ask
- **Funding Needs**: Pre-seed / Non-dilutive grant funding (€150k–€350k) to fund:
  - Mobile engineering and real-time WebSocket backend infrastructure.
  - Regulatory compliance, insurance sandbox coverage, and municipal pilot permits.
  - Corridor-specific initial driver seeding incentives.
