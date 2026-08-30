# HopOn — Founding Team & Contributor Specification

> **Mission**: Build the core founding team to advance HopOn from an established algorithmic proof-of-concept into live corridor pilot deployments.

---

## 1. Team Architecture

As an AI-assisted solo inventor project, HopOn's transition to a high-velocity startup requires complementary founding talent across two core pillars:

`
                  ┌───────────────────────────────┐
                  │    Founder / Lead Architect   │
                  │        (Slavko Stojnić)       │
                  │   IP, System Design, Backend  │
                  └───────────────┬───────────────┘
                                  │
         ┌────────────────────────┴────────────────────────┐
         │                                                 │
┌────────▼───────────────────────┐       ┌─────────────────▼────────────────┐
│  Technical Co-Founder / Mobile │       │  Operations & Growth Co-Founder  │
│  React Native / Flutter / Maps │       │  Transit Policy, Pilots & Safety │
└────────────────────────────────┘       └──────────────────────────────────┘
`

---

## 2. Target Roles & Profiles

### Role A: Technical Co-Founder / Lead Mobile Engineer
- **Core Responsibility**: Own the passenger and driver mobile applications, real-time map interfaces, geolocation telemetry, and color-code visual handshake protocols.
- **Ideal Background**:
  - 3+ years experience building production React Native or Flutter applications.
  - Deep experience with mobile location services: background location tracking, geofencing, battery-efficient GPS polling, and map SDKs (Mapbox GL, Google Maps, OpenStreetMap).
  - Familiarity with WebSocket / real-time messaging architecture.
- **Initial Milestone**: Deliver cross-platform passenger and driver MVP client that communicates with the HopOn route matching engine.

### Role B: Operations & City Pilot Lead (Co-Founder / Head of Ops)
- **Core Responsibility**: Regulatory compliance, carpooling legal frameworks, municipal transport sandbox agreements, and driver community onboarding along initial test corridors.
- **Ideal Background**:
  - Experience in shared mobility, micromobility (e-scooters/bikes), delivery logistics, or urban transit planning.
  - Familiarity with transportation regulatory sandboxes and non-commercial carpooling legislation (cost-sharing exemptions under taxi regulations).
  - Strong community-building and ground-game execution.
- **Initial Milestone**: Secure municipal sandbox approval or university/business park partnership for a 30-day closed corridor pilot.

---

## 3. Equity & Compensation Framework
- **Pre-Funding**: Significant co-founder equity allocation (15%–35% depending on commitment, role, and capital contribution) structured with standard 4-year vesting and 1-year cliff.
- **Post-Funding**: Market salary benchmarked to pre-seed / seed funding tranches + equity retention.
- **Alignment with APC & IPClaim**: All intellectual property developed for HopOn is assigned to the operating corporate entity, respecting the author's provenance and baseline architecture.

---

## 4. Contributor Trial Challenge (Proof of Skill)
Prospective technical contributors and co-founder candidates are invited to demonstrate capability through a practical, open-source pull request:

1. **The Challenge**: Implement a simple mobile or web client proof-of-concept connecting to the ackend/matching.py and ackend/pickup.py modules.
2. **Evaluation Criteria**:
   - Clean, idiomatic code and intuitive UI.
   - Elegant visualization of route corridor, safe pickup offsets, and the 30-second countdown / color-code handshake.
   - Comprehensive test coverage.
3. **How to Apply**:
   - Review [DoD.md](../DoD.md) and [BACKLOG.md](../BACKLOG.md).
   - Submit a pull request on GitHub or open an issue titled [Candidate] Co-Founder Interest — [Your Name].
