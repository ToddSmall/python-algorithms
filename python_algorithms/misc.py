"""An assortment of solutions to easy CS problems."""

from typing import List, Generator, Tuple


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
