def post_charge(key, payload, ledger):
    """Defective first revision: duplicate requests create separate charges."""
    result = {"charge_id": len(ledger) + 1, "payload": payload}
    ledger[str(len(ledger) + 1)] = result
    return result


def charge_count(ledger):
    return len(ledger)
