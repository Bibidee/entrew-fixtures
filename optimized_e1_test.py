import pytest
from optimized_e1_charges import create_charge


def test_matching_key_replays_original_response():
    first = create_charge("customer-1", 100, "key-1")
    replay = create_charge("customer-1", 100, "key-1")
    assert first is replay


def test_matching_key_rejects_changed_payload():
    create_charge("customer-1", 100, "key-1")
    with pytest.raises(ValueError, match="different payload"):
        create_charge("customer-1", 200, "key-1")