from live_e4_charges import create_charge


def test_matching_key_replays_the_original_charge():
    first = create_charge("customer-1", 100, "key-1")
    replay = create_charge("customer-1", 100, "key-1")
    assert replay is first
    assert replay["charge_id"] == "customer-1:key-1"


def test_conflicting_payload_is_rejected():
    create_charge("customer-1", 100, "key-2")
    try:
        create_charge("customer-1", 101, "key-2")
    except ValueError:
        return
    raise AssertionError("conflicting idempotency-key payload was accepted")
