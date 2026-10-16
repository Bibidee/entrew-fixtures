def post_charge(key, payload, ledger):
    # Deliberately defective revision: it creates a new charge every time and
    # never records the idempotency key.
    result = {"charge_id": len(ledger) + 1, "payload": payload}
    ledger[str(len(ledger) + 1)] = result
    return result


def charge_count(ledger):
    return len(ledger)
