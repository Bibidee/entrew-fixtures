# Idempotency behavior

`post_charge` records the first request by idempotency key. A later request
with that same key and the same payload returns the saved charge, so it does
not create a second charge. Reusing a key with a different payload raises
`IdempotencyConflict` and leaves the existing charge unchanged.
