import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from charges import IdempotencyConflict, charge_count, post_charge


class PositiveIdempotencyTests(unittest.TestCase):
    def test_same_key_replays_one_charge(self):
        ledger = {}
        payload = {"amount": 100, "currency": "USD"}
        first = post_charge("positive-fresh-key", payload, ledger)
        self.assertEqual(post_charge("positive-fresh-key", payload, ledger), first)
        self.assertEqual(charge_count(ledger), 1)

    def test_key_cannot_bind_different_payload(self):
        ledger = {}
        post_charge("positive-conflict-key", {"amount": 100}, ledger)
        with self.assertRaises(IdempotencyConflict):
            post_charge("positive-conflict-key", {"amount": 200}, ledger)


if __name__ == "__main__":
    unittest.main()
