from backend.payments import PaymentProviderStub


def test_payments_stub_records():
    p = PaymentProviderStub()
    c = p.charge_passenger("p1", 100.0)
    assert c["status"] == "charged"
    assert len(p.charges) == 1
    pay = p.payout_driver("d1", 80.0)
    assert pay["status"] == "paid"
    assert len(p.payouts) == 1
