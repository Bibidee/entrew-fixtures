def create_charge(customer, amount_cents, idempotency_key):
    """Defective fixture: reuses key without replay storage."""
    return {"customer": customer, "amount_cents": amount_cents, "idempotency_key": idempotency_key, "charge_id": f"{customer}:{idempotency_key}"}
