def create_charge(customer, amount_cents, idempotency_key):
    """Defective baseline: matching keys create a second charge."""
    return {
        "customer": customer,
        "amount_cents": amount_cents,
        "idempotency_key": idempotency_key,
        "charge_id": f"{customer}:{idempotency_key}",
    }
