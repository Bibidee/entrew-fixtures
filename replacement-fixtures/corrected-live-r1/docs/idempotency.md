# Idempotency-key behaviour

Matching idempotency-key requests replay one stored charge. Reusing an existing
key with a different payload is rejected as an idempotency conflict.
