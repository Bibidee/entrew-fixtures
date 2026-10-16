def normalize_tag(value: str) -> str:
    if not isinstance(value, str):
        raise TypeError("value must be a string")
    return value.lower()
