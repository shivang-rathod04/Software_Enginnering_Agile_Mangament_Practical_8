
import pytest
from budget import remaining_budget

def test_remaining_budget():
    assert remaining_budget(1000, 250) == 750

def test_zero_spent():
    assert remaining_budget(1000, 0) == 1000

def test_overspending_is_negative():
    assert remaining_budget(1000, 1200) == -200

def test_invalid_negative_values():
    with pytest.raises(ValueError):
        remaining_budget(-100, 10)
