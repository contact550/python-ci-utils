import pytest
from src.processor import normalize_numbers, filter_outliers, calculate_statistics

@pytest.mark.parametrize("nums, expected", [
    ([10, 20, 30], [0.0, 0.5, 1.0]),
    ([5, 5, 5], [0.0, 0.0, 0.0])
])
def test_normalize(nums, expected):
    assert normalize_numbers(nums) == expected

def test_normalize_error():
    with pytest.raises(ValueError):
        normalize_numbers([])

@pytest.mark.parametrize("nums, low, high, exp", [
    ([1, 5, 10], 2, 6, [5]),
    ([1, 2, 3], 10, 20, [])
])
def test_filter(nums, low, high, exp):
    assert filter_outliers(nums, low, high) == exp

def test_stats():
    res = calculate_statistics([1, 2, 3])
    assert res["min"] == 1
    assert res["average"] == 2.0
