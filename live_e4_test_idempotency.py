from live_e4_charges import create_charge


def test_defective_baseline_creates_another_charge_for_a_matching_key():
    first = create_charge("customer-1", 100, "key-1")
    replay = create_charge("customer-1", 100, "key-1")
    assert first is not replay
    assert replay["created"] is True
