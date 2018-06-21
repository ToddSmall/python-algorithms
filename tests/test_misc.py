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
