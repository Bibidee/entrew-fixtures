# Negative evidence

This implementation does not persist or replay idempotency keys. Matching requests create independent response objects, so the implementation fails the required replay behavior.
