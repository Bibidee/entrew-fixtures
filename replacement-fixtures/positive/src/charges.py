class IdempotencyConflict(ValueError):
    pass


def post_charge(key, payload, ledger):
    if key in ledger:
        saved_payload, result = ledger[key]
        if saved_payload != payload:
            raise IdempotencyConflict("idempotency key was reused with different data")
        return result
    result = {"charge_id": len(ledger) + 1, "payload": payload}
    ledger[key] = (payload, result)
    return result


def charge_count(ledger):
    return len(ledger)
