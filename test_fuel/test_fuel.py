import pytest
from pytest import raises
from fuel import gauge, convert

def test_gauge():
    assert gauge(0)=='E'
    assert gauge(1)=='E'
    assert gauge(99)=='F'
    assert gauge(100)=='F'
    assert gauge(50)=='50%'
    assert gauge(10)=='10%'

def test_convert():
    assert convert("5/10")==50
    assert convert("10/10")==100
    assert convert("47/100")==47

def test_valueerror():
    with raises(ValueError):
        convert("150/100")
        convert("cat/dog")

def test_zero():
    with raises(ZeroDivisionError):
        convert("100/0")
