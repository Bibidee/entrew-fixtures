import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from charges import charge_count, post_charge


class CorrectedRevisionOneTests(unittest.TestCase):
    def test_same_key_creates_duplicate_charges_in_this_defective_revision(self):
        ledger = {}
        payload = {"amount": 100, "currency": "USD"}
        first = post_charge("corrected-r1-fresh-key", payload, ledger)
        second = post_charge("corrected-r1-fresh-key", payload, ledger)
        self.assertNotEqual(first, second)
        self.assertEqual(charge_count(ledger), 2)


if __name__ == "__main__":
    unittest.main()
