"""Solving a few dynamic programming problems"""

from functools import wraps
import sys
from typing import Callable, List, Tuple


def memoized(f: Callable) -> Callable:
    """Decorator that memoizes the wrapped function."""
    cache = {}
    @wraps(f)
    def wrapped(*args):
        try:
            result = cache[args]
        except KeyError:
            result = cache[args] = f(*args)
        return result
    return wrapped


def cut_rod(prices: List[float], rod_length: int) -> float:
    @memoized
    def _cut_rod(rod_length):
        if rod_length == 0:
            return 0

        revenue = -sys.maxsize
        for i in range(1, rod_length+1):
            revenue = max(revenue, prices[i-1] + _cut_rod(rod_length-i))

        return revenue

    return _cut_rod(rod_length)


def knapsack(items: List[Tuple[int, int]], max_weight: int) -> Tuple[int, List[Tuple[int, int]]]:
    """The classic 0/1 knapsack problem.

    https://en.wikipedia.org/wiki/Knapsack_problem#0.2F1_knapsack_problem
    http://codereview.stackexchange.com/a/20581
    """
    @memoized
    def best_value(i: int, w: int) -> int:
        """Return the best value that can be attained using the
        first i items with weight <= w.
        """
        if i == 0:
            return 0

        value, weight = items[i - 1]

        if weight > w:
            return best_value(i - 1, w)

        return max(best_value(i - 1, w), best_value(i - 1, w - weight) + value)

    # This code block is only necessary for listing the items.
    # The best value can be, and is, computed without this
    # code block.
    w = max_weight
    result = []
    for i in range(len(items), 0, -1):
        if best_value(i, w) != best_value(i - 1, w):
            result.append(items[i - 1])
            w -= items[i - 1][1]
    result.reverse()

    return best_value(len(items), max_weight), result
