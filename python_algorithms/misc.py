"""An assortment of solutions to easy CS problems."""

from itertools import groupby
from typing import List, Generator, Sequence, Tuple


def gen_product_pairs(
    xs: List[float], prod: float
) -> Generator[Tuple[float, float], None, None]:
    """Search the list `xs` for pairs whose product equals `prod`.

    https://codereview.stackexchange.com/a/84721
    """
    factors: set = set()
    for x in xs:
        if x in factors:
            yield prod / x, x
        else:
            factors.add(prod / x)


def max_sub_array(xs: Sequence[int]) -> List[int]:
    """Find the maximum subarray of non-negative numbers in an array.Sequence

    https://codereview.stackexchange.com/a/193912
    """
    sub_arrs = (list(g) for non_negative, g in groupby(xs, key=lambda x: x >= 0) if non_negative)
    return max(sub_arrs, key=lambda arr: (sum(arr), len(arr)), default=[])
