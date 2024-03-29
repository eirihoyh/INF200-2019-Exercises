# -*- coding: utf-8 -*-

__author__ = "Eirik Høyheim"
__email__ = "eirihoyh@nmbu.no"

import pytest


@pytest.fixture
def fixed_data_list():
    return [1, 4, 7, 9, 3]


def median(data):
    """
    Returns median of data.

    :param data: An iterable of containing numbers
    :return: Median of data
    """

    sdata = sorted(data)
    n = len(sdata)
    if n == 0:
        raise ValueError
    return (
        sdata[n // 2]
        if n % 2 == 1
        else 0.5 * (sdata[n // 2 - 1] + sdata[n // 2])
    )


def test_median_of_singeleton():
    """Tests if the median of a list just containing 4 is 4"""
    assert median([4]) == 4


def test_median_odd_numbers():
    """Test if the median function can find the median of a list with odd
    numbers """
    assert median([1, 3, 5, 7, 9]) == 5


def test_median_even_numbers():
    """Tests if the median function can find the median of list with even
    numbers """
    assert median([2, 4, 6, 8, 10, 12]) == 7


def test_median_with_ordered_numbers():
    """Tests if the meidian function can find the median of a list with
    ordered numbers """
    assert median([1, 2, 3, 4, 5, 6, 7]) == 4


def test_median_with_reverse_order():
    """Checks if the median function can find the median of a list with
    reverse order """
    assert median([7, 6, 5, 4, 3, 2, 1]) == 4


def test_median_unordered():
    """Checks if the median function can find the median of a list that is
    out of order """
    assert median([2, 4, 1, 3, 6]) == 3


def test_median_rasis_value_error_on_empty_list():
    """Checks if the median raises a ValueError when the list is empty"""
    with pytest.raises(ValueError):
        median([])


def test_median_does_not_change_org_data(fixed_data_list):
    """Checks if the median function does not change the original data.
    Made a fixed_data_list that I use to have a standard list."""
    data = fixed_data_list
    median(data)
    assert data == fixed_data_list


def test_median_for_tuplets():
    """Checks if the can take in a tuplet list and get the same results as
    if they were lists """
    data_tuplet = (1, 2, 3, 4, 5)
    data_list = [1, 2, 3, 4, 5]
    assert median(data_tuplet) == median(data_list)
