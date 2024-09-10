from working import convert
import pytest

def test_convert():
    assert convert("9 AM to 5 PM")=="09:00 to 17:00"
    assert convert("9:20 AM to 5 PM")=="09:20 to 17:00"
    assert convert("9 AM to 5:20 PM")=="09:00 to 17:20"
    assert convert("9:01 AM to 5:40 PM")=="09:01 to 17:40"
    with pytest.raises(ValueError):
        convert("13 AM to 5 PM")
    with pytest.raises(ValueError):
        convert("9 AM 5 PM")
    with pytest.raises(ValueError):
        convert("11:60 AM to 5:30 PM")


