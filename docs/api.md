# HopOn — local pilot API

Run `python hopon_app.py` and open http://127.0.0.1:8787.

All responses are JSON. Every driver registration and ride request returns a random session token; subsequent operations use it in the `X-HopOn-Token` header. Browser UI manages these automatically.

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/api/health` | Check local server |
| POST | `/api/drivers` | Register driver with `route`, optional `position`, `label`, `seats` |
| POST | `/api/drivers/{id}` | Update position or `online` state (driver token) |
| GET | `/api/drivers/{id}/rides` | List driver's active assignments (driver token) |
| POST | `/api/rides` | Request a trip with `origin`, `destination` |
| GET | `/api/rides/{id}` | See assignment and pickup (passenger/assigned driver token) |
| POST | `/api/rides/{id}` | Update walking passenger position via `origin` (passenger token) |
| POST | `/api/rides/{id}/action` | Perform `cancel`, `board`, `decline`, or `complete` (authorized session) |

Coordinates are `[latitude, longitude]`. A driver route is an ordered list of 2–100 waypoints. A matching route must pass within 250 m of the passenger and 100 m of their destination, and continue forward past the pickup. The driver must be on the route and online.

The 30-second waiting countdown starts when the driver reaches within 35 meters of the suggested meeting point. Expired assignments are excluded and alternate drivers considered. Seats are reserved while assigned/boarded. Price is based on distance traveled as a passenger (currently a configurable example, not a charge).

Example driver registration:

```json
{"route":[[59.32,18.05],[59.32,18.06],[59.32,18.075],[59.32,18.09]],"seats":1,"label":"Blue hatchback"}
```

Example passenger trip:

```json
{"origin":[59.32,18.065],"destination":[59.32,18.086]}
```

**Local-only pilot.** Tokens are unverified sessions, not personal identity verification. Data is held in process memory, with no durable storage. No production authentication, TLS termination, real payment transfers, verified safe pickup zones, road routing, insurance, or driver screening is implemented. The API must remain on localhost or an explicitly trusted test network.
