from um import count
import pytest

def test_single_um():
    assert count("um")==1
    assert count("  um  ")==1
    assert count("um?")==1


def test_case_sensitivity():
    assert count("UM")==1
    assert count("Um Um um UM")==4
    assert count("Um, I have to, um, do this um.")==3

def test_no_um():
    assert count("")==0
    assert count("haha, no word here")==0

def test_um_in_middle():
    assert count("umbrella")==0
    assert count("yummy")==0

