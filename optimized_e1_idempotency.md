# Idempotency behavior

A request with a matching idempotency key replays the one original charge. Reusing
that key with different customer or amount data is rejected and never creates a
second charge.
