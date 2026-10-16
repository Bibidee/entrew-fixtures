# Replacement fixture sources

These replacements repair incomplete test code in the historical positive and
corrected revisions. The positive source is now bound by the branch-tip marker
to the separately deployed corrected contract's `p1` program, the authorized
positive applicant, and a fresh nonce. The frozen `entrew-live-2026-10-16`
commits remain unchanged.

Run each replacement with Python from the repository root:

```text
python replacement-fixtures/positive/tests/test_idempotency.py
python replacement-fixtures/corrected-r1/tests/test_idempotency.py
python replacement-fixtures/corrected-r2/tests/test_idempotency.py
```
