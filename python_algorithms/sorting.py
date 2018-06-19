"""Implementing some sorting and order statistics algorithms."""

from abc import abstractmethod
from typing import Any, MutableSequence, TypeVar
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
            A[j+1] = A[j]
            j = j - 1
        A[j+1] = key
    return None


# Routines associated with max- and min-heaps
def get_index_of_parent(i: int) -> int:
    """Return the index of the parent of the node i."""
    return (i-1) // 2


def get_index_of_left_child(i: int) -> int:
    """Return the left child of the node i."""
    return 2*i + 1


def get_index_of_right_child(i: int) -> int:
    """Return the right child of the node i."""
    return 2*i + 2


def max_heapify(A: MutableSequence[CT], i: int) -> None:
    """Rearrange the elements of A, starting from node i, into a heap."""
    left = get_index_of_left_child(i)
    right = get_index_of_right_child(i)
    if left < len(A) and A[left] > A[i]:
        largest = left
    else:
        largest = i
    if right < len(A) and A[right] > A[largest]:
        largest = right
    if largest == i:
        return None
    A[i], A[largest] = A[largest], A[i]
    return max_heapify(A, largest)
