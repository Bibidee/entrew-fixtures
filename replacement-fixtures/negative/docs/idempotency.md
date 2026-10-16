# Idempotency-key behaviour

A matching idempotency key and payload must replay the original charge so a
caller never creates a second charge. Reusing the key with a different payload
must be rejected as a conflict.
