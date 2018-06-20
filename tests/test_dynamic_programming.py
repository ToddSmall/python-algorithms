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


@pytest.mark.parametrize("num_rolls, sum_rolls, expected", [
    (2, 3, 2),
    (3, 2, 0),
    (3, 3, 1),
    (3, 8, 21),
    (3, 10, 27),
    (5, 17, 780),
])
def test_dice_rolls(num_rolls, sum_rolls, expected):
    assert dp.dice_rolls(num_rolls, sum_rolls) == expected


def test_knapsack():
    items = [(4, 12), (2, 1), (6, 4), (1, 1), (2, 2)]
    max_weight = 15
    expected = (11, [(2, 1), (6, 4), (1, 1), (2, 2)])
    assert dp.knapsack(items, max_weight) == expected


@pytest.mark.parametrize("total, G, expected", [
    (7, [[0, 2, 5], [1, 1, 3], [2, 1, 1]], 0),
    (12, [[0, 2, 5], [1, 1, 3], [2, 1, 1]], 1),
])
def test_min_remainder(total, G, expected):
    i = j = len(G[0])
    assert dp.min_remainder(i, j, total, G) == expected
