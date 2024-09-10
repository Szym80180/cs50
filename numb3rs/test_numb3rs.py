import pytest
from numb3rs import validate

def test_validate():
    assert validate("1.1.1.1") == True
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("128.128.128.128") == True
    assert validate("500.1.1.1") == False
    assert validate("1.500.1.1") == False
    assert validate("1.1.500.1") == False
    assert validate("1.1.1.500") == False
    assert validate("-1.1.11.1") == False
    assert validate("cat") == False
    assert validate("1.1.1.1.1")==False
    assert validate("1.1.1.1.")==False



