_CHARGES = {}


def create_charge(customer, amount_cents, idempotency_key):
    """Replay matching idempotency keys and reject changed payloads."""
    payload = (customer, amount_cents)
    existing = _CHARGES.get(idempotency_key)
    if existing is not None:
        if existing["payload"] != payload:
            raise ValueError("idempotency key cannot be reused with a different payload")
        return existing["response"]
    response = {
        "customer": customer,
        "amount_cents": amount_cents,
        "idempotency_key": idempotency_key,
        "charge_id": f"{customer}:{idempotency_key}",
    }
    _CHARGES[idempotency_key] = {"payload": payload, "response": response}
    return response