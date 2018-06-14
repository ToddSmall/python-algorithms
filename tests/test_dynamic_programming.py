import pytest

import python_algorithms.dynamic_programming as dp


@pytest.mark.parametrize("rod_length, expected", [
    (4, 10),
    (5, 13),
    (6, 17),
    (9, 25),
    (10, 30),
])
def test_cut_rod(rod_length, expected):
    prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    assert dp.cut_rod(prices, rod_length) == expected


def test_knapsack():
    items = [(4, 12), (2, 1), (6, 4), (1, 1), (2, 2)]
    max_weight = 15
    expected = (11, [(2, 1), (6, 4), (1, 1), (2, 2)])
    assert dp.knapsack(items, max_weight) == expected
