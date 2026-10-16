from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))
from charges import charge_count, post_charge


def test_first_revision_demonstrates_the_duplicate_charge_defect():
    ledger = {}
    assert post_charge("key", {"amount": 5}, ledger) != post_charge("key", {"amount": 5}, ledger)
    assert charge_count(ledger) == 2
