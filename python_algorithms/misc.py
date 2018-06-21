"""An assortment of solutions to easy CS problems."""

from typing import List, Tuple


def gen_product_pairs(xs: List[float], prod: float) -> List[Tuple[float, float]]:
    """Search the list `xs` for pairs whose product equals `prod`."""
    factors = set()
    for x in xs:
        if x in factors:
            yield prod / x, x
        else:
            factors.add(prod / x)
        
