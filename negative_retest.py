def create_charge(customer, amount_cents, idempotency_key):
    # Deliberately violates replay and conflict-rejection requirements.
    return {"charge_id": f"new:{customer}:{amount_cents}:{idempotency_key}", "customer": customer, "amount_cents": amount_cents}
