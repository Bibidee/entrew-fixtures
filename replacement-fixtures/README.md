# Replacement fixture sources

These source-only replacements repair incomplete test code in the historical
positive and corrected revisions. They deliberately do not add or change an
ENTREW claim marker: a later, separately authorized lifecycle run must create a
new marker commit that binds its new program ID, applicant wallet, and fresh
nonce. The frozen `entrew-live-2026-10-16` commits remain unchanged.

Run each replacement with Python from the repository root:

```text
python replacement-fixtures/positive/tests/test_idempotency.py
python replacement-fixtures/corrected-r1/tests/test_idempotency.py
python replacement-fixtures/corrected-r2/tests/test_idempotency.py
```
