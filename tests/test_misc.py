"""Tests of solutions to various easy CS problems."""

import pytest

from python_algorithms import misc


@pytest.mark.parametrize(
    "xs, prod, expected",
    [
        ([12, -4, 6, 4, 5, 7, 2], 24, [(6, 4), (12, 2)]),
        ([12, -4, 6, 4, 5, 7, 2], 25, []),
    ],
)
def test_gen_product_pairs(xs, prod, expected):
    assert list(misc.gen_product_pairs(xs, prod)) == expected


@pytest.mark.parametrize(
    "xs, expected",
    [([-6, -8, -12, -5], []), ([1, 2, 5, -7, 2, 5], [1, 2, 5])]
)
def test_max_sub_array(xs, expected):
    assert misc.max_sub_array(xs) == expected
