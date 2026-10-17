from optimized_e1_charges import create_charge


def test_baseline_is_defective():
    first = create_charge("customer-1", 100, "key-1")
    replay = create_charge("customer-1", 100, "key-1")
    assert first is not replay
    assert first == replay
