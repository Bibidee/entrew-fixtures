from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))
from charges import charge_count, post_charge


def test_fixture_exposes_the_intentional_duplicate_charge_defect():
    ledger = {}
    first = post_charge("same-key", {"amount": 7}, ledger)
    second = post_charge("same-key", {"amount": 7}, ledger)
    assert first != second
    assert charge_count(ledger) == 2
