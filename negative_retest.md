# Explicit negative evidence

The handler always creates a new response and keeps no idempotency store. A matching key therefore does not replay any original charge, and changed payload reuse is accepted rather than rejected.
