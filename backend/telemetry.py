"""Simple telemetry utilities (request-scoped logging).

Provides a tiny helper to format logs with a request id so matching decisions
can be replayed from logs.
"""
import logging

logger = logging.getLogger("hopon")
if not logger.handlers:
    handler = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)


def log_request(request_id: str, message: str, level: str = "info"):
    msg = f"req={request_id} {message}"
    if level == "debug":
        logger.debug(msg)
    elif level == "warning":
        logger.warning(msg)
    else:
        logger.info(msg)
