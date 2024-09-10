import pytest

from plates import is_valid

def test_length():
    assert is_valid("A")==False
    assert is_valid("AAAAAAA")==False
    assert is_valid("ABCDEFGHIJK")==False
    assert is_valid("ABCDEF")==True
    assert is_valid("ABCDE")==True
    assert is_valid("ABCD")==True
    assert is_valid("ABC")==True
    assert is_valid("AB")==True


def test_two_letters_start():
    assert is_valid("AB1234")==True
    assert is_valid("ABABA")==True
    assert is_valid("ABABA1")==True
    assert is_valid("123456")== False
    assert is_valid("A12345")==False
    assert is_valid("A1ABAB")==False
    assert is_valid("1ABCDE")==False
    assert is_valid("12")==False
    assert is_valid("A1")==False
    assert is_valid("AA1")==True

def test_numbers_in_middle():
    assert is_valid("AB1234")==True
    assert is_valid("AB12AB")==False
    assert is_valid("AB1A2B")==False
    assert is_valid("AB1AB2")==False

def test_first_zero():
    assert is_valid("AB1234")==True
    assert is_valid("AB10")==True
    assert is_valid("AB0123")==False
    assert is_valid("AB0")==False
    assert is_valid("AB01")==False

def test_punctuation():
    assert is_valid("AB AB")==False
    assert is_valid("AB.AB")==False
    assert is_valid("AB,01")==False
    assert is_valid("ABAB")==True

