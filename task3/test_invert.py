import pytest
from inverter import invert


# CORRECT IMPLEMENTATION
def test_invert_pass_empty_string():
    assert invert("") == ""

def test_invert_pass_none():
    assert invert() == ""

def test_invert_pass_single_char():
    assert invert("a") == "a"

def test_invert_pass_multiple_char():
    assert invert("abcd") == "dcba"

# WRONG IMPLEMENTATION
def test_invert_fail_empty_string():
    assert invert("") != ""

def test_invert_fail_none():
    assert invert() != ""

def test_invert_fail_single_char():
    assert invert("a") != "a"

def test_invert_fail_multiple_char():
    assert invert("abcd") != "dcba"