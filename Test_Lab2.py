# test_lab2.py

from Lab2 import calc_average, find_min_max, calc_median_temperature

def test_find_min_max():
    # Test case with positive numbers
    numlist_positive = [4, 8, 2, 10, 5]
    result_positive = find_min_max(numlist_positive)
    assert result_positive == ["Minimum value = 2", "Maximum value = 10"]

    # Test case with negative numbers
    numlist_negative = [-4, -8, -2, -10, -5]
    result_negative = find_min_max(numlist_negative)
    assert result_negative == ["Minimum value = -10", "Maximum value = -2"]

    # Test case with mixed positive and negative numbers
    numlist_mixed = [-4, 8, -2, 10, -5]
    result_mixed = find_min_max(numlist_mixed)
    assert result_mixed == ["Minimum value = -5", "Maximum value = 10"]

    # Test case with duplicate values
    numlist_duplicates = [4, 8, 2, 10, 5, 10, 2]
    result_duplicates = find_min_max(numlist_duplicates)
    assert result_duplicates == ["Minimum value = 2", "Maximum value = 10"]

def test_calc_average():
    # Test case with positive numbers
    numlist_positive = [4, 8, 2, 10, 5]
    result_positive = calc_average(numlist_positive)
    assert result_positive == 5.8

    # Test case with negative numbers
    numlist_negative = [-4, -8, -2, -10, -5]
    result_negative = calc_average(numlist_negative)
    assert result_negative == -5.8

    # Test case with mixed positive and negative numbers
    numlist_mixed = [-4, 8, -2, 10, -5]
    result_mixed = calc_average(numlist_mixed)
    assert result_mixed == 1.4

    # Test case with duplicate values
    numlist_duplicates = [4, 8, 2, 10, 5, 10, 2]
    result_duplicates = calc_average(numlist_duplicates)
    assert result_duplicates == 5.857142857142857  # The average of these numbers

def test_calc_median_temperature():
    # Test case with even number of elements
    numlist_even = [4, 8, 2, 10, 5, 6]
    result_even = calc_median_temperature(numlist_even)
    assert result_even == 5.5

    # Test case with odd number of elements
    numlist_odd = [4, 8, 2, 10, 5]
    result_odd = calc_median_temperature(numlist_odd)
    assert result_odd == 5.0

    # Test case with negative numbers
    numlist_negative = [-4, -8, -2, -10, -5]
    result_negative = calc_median_temperature(numlist_negative)
    assert result_negative == -5.0

    # Test case with duplicate values
    numlist_duplicates = [4, 8, 2, 10, 5, 10, 2]
    result_duplicates = calc_median_temperature(numlist_duplicates)
    assert result_duplicates == 5.0  # The median of these numbers

if __name__ == '__main__':
    test_find_min_max()
    print("All tests passed!")
