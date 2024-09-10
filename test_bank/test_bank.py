import pytest

from bank import value

def test_value_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HeLlO") == 0

def test_value_h():
    assert value("h") == 20
    assert value("hulajhulaj") == 20
    assert value("HI") == 20
    assert value("hULAJ") == 20

def test_value_other():
    assert value("other")==100
    assert value("OTHERCAPS")==100
    assert value("containsh")==100
    assert value("containsH")==100
