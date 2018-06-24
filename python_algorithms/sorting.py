"""Implementing some sorting and order statistics algorithms."""

from abc import abstractmethod
import math
import random
from typing import Any, MutableSequence, Optional, TypeVar
from typing_extensions import Protocol


class Comparable(Protocol):
    @abstractmethod
    def __lt__(self, other: Any):
        pass


CT = TypeVar("CT", bound=Comparable)


def insertion_sort(A: MutableSequence[CT]) -> None:
    """A O(n^2) sorting algorithm."""
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = key
    return None


# Routines associated with max- and min-heaps
def get_index_of_parent(i: int) -> int:
    """Return the index of the parent of the node i."""
    return (i - 1) // 2


def get_index_of_left_child(i: int) -> int:
    """Return the left child of the node i."""
    return (2 * i) + 1


def get_index_of_right_child(i: int) -> int:
    """Return the right child of the node i."""
    return (2 * i) + 2


def get_first_leaf_index(len_heap: int) -> int:
    """Return the small index of a heap leaf node."""
    return math.ceil((len_heap - 1) / 2)


def max_heapify(
    A: MutableSequence[CT], i: int, heap_size: Optional[int] = None
) -> None:
    """Rearrange the elements of A, starting from node i, into a heap."""
    if heap_size is None:
        heap_size = len(A) - 1
    left = get_index_of_left_child(i)
    right = get_index_of_right_child(i)
    if left <= heap_size and A[left] > A[i]:
        largest = left
    else:
        largest = i
    if right <= heap_size and A[right] > A[largest]:
        largest = right
    if largest == i:
        return None
    A[i], A[largest] = A[largest], A[i]
    return max_heapify(A, largest, heap_size=heap_size)


def build_max_heap(A: MutableSequence[CT]) -> None:
    """Transform `A` into a max-heap."""
    last_not_leaf_index = get_first_leaf_index(len(A)) - 1
    for i in range(last_not_leaf_index, -1, -1):
        max_heapify(A, i)


def heap_sort(A: MutableSequence[CT]) -> None:
    """O(n log n) in place sort of `A` using a heap data structure."""
    len_A = len(A)
    heap_size = len_A - 1
    build_max_heap(A)
    for i in range(len_A - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heap_size = heap_size - 1
        max_heapify(A, 0, heap_size=heap_size)


def partition(
    A: MutableSequence[CT], p: Optional[int] = None, r: Optional[int] = None
) -> int:
    """Partition `A[p:r]`.

    `A[p:r]` is partitioned into two arrays, `A[p:q]` and `A[q+1:r]`, such
    that each element of `A[p:q]` is <= A[q] and each element of `A[q+1:r]` is
    >= to A[q]. Returns the index `q`.
    """
    if p is None:
        p = 0
    if r is None:
        r = len(A) - 1
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def randomized_partition(
    A: MutableSequence[CT], p: Optional[int] = None, r: Optional[int] = None
) -> int:
    if p is None:
        p = 0
    if r is None:
        r = len(A) - 1
    i = random.randint(p, r)
    A[i], A[r] = A[r], A[i]
    return partition(A, p, r)


def quick_sort(
    A: MutableSequence[CT], p: Optional[int] = None, r: Optional[int] = None
) -> None:
    """O(n log n) in place sort of `A`."""
    if p is None:
        p = 0
    if r is None:
        r = len(A) - 1
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)


def randomized_select(
    A: MutableSequence[CT], i: int, p: Optional[int] = None, r: Optional[int] = None
) -> int:
    """O(n) search for the i-th smallest element of `A[p:r+1]`."""
    if p is None:
        p = 0
    if r is None:
        r = len(A) - 1
    if p >= r:
        return A[r]
    q = randomized_partition(A, p, r)
    k = q - p + 1
    if k == i:
        return A[q]
    if i < k:
        return randomized_select(A, i, p, q - 1)
    return randomized_select(A, i - k, q + 1, r)
