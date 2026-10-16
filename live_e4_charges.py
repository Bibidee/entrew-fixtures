def create_charge(customer, amount_cents, idempotency_key):
    """Defective baseline: a matching key is charged again instead of replayed."""
    return {"customer": customer, "amount_cents": amount_cents, "idempotency_key": idempotency_key, "created": True}
