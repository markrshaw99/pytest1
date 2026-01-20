import pytest
from lib.present import Present

def test_present():
    present1 = Present()
    with pytest.raises(Exception) as e1:
        present1.unwrap()
    assert str(e1.value) == "No contents have been wrapped."
    present1.wrap("Blueberries")
    with pytest.raises (Exception) as e2:
        present1.wrap("Strawberries")
    assert str(e2.value) == "A contents has already been wrapped."
    assert present1.unwrap() == "Blueberries"
