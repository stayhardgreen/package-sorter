# test_sorter.py

import pytest
from sorter import sort

def test_standard():
    assert sort(10, 10, 10, 1) == "STANDARD"

def test_bulky_by_volume_exact_threshold():
    assert sort(100, 100, 100, 1) == "SPECIAL"

def test_bulky_by_dimension_exact_threshold():
    assert sort(150, 10, 10, 1) == "SPECIAL"

def test_heavy_exact_threshold():
    assert sort(10, 10, 10, 20) == "SPECIAL"

def test_rejected_when_both():
    assert sort(150, 100, 100, 20) == "REJECTED"

def test_non_integer_inputs():
    assert sort(149.9, 149.9, 44.6, 19.99) == "STANDARD"

def test_negative_inputs_raise():
    with pytest.raises(ValueError):
        sort(-1, 10, 10, 1)

def test_none_inputs_raise():
    with pytest.raises(ValueError):
        sort(None, 10, 10, 1)
