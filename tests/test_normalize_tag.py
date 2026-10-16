from src.normalize_tag import normalize_tag

def test_normalizes_mixed_case_and_outer_spaces():
    assert normalize_tag("  GenLayer  ") == "genlayer"

def test_collapses_repeated_internal_spaces():
    assert normalize_tag("ENTREW   Registry") == "entrew registry"
