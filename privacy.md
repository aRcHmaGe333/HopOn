# Privacy & Data Retention

This document summarizes the minimal privacy guarantees for the HopOn MVP.

- Location telemetry (trip traces, pickup points): retained for 30 days by default for safety investigations and fraud detection.
- Personal identifiers (names, emails): retained for 365 days for dispute resolution unless user requests deletion.
- Aggregated anonymized telemetry (usage, heatmaps): retained indefinitely for analytics.

Access to raw telemetry is restricted to authorized personnel and supervisors. For production deployments, integrate a secure storage and deletion workflow and document it in `docs/dev-setup.md`.
