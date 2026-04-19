"""Payments sandbox stub for HopOn MVP.

This module provides a simple in-memory stub that simulates charging a
passenger and crediting a driver. It is intentionally simple and only used
for testing the payment flow during development.
"""
from typing import List, Dict


class PaymentProviderStub:
    def __init__(self):
        self.charges: List[Dict] = []
        self.payouts: List[Dict] = []

    def charge_passenger(self, passenger_id: str, amount: float) -> Dict:
        record = {"passenger_id": passenger_id, "amount": float(amount), "status": "charged"}
        self.charges.append(record)
        return record

    def payout_driver(self, driver_id: str, amount: float) -> Dict:
        record = {"driver_id": driver_id, "amount": float(amount), "status": "paid"}
        self.payouts.append(record)
        return record
