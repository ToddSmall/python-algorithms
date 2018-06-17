"""Tests of sorting algorithms implemented in Python."""

import pytest

from python_algorithms.sorting import (insertion_sort,
                                       get_index_of_parent,
                                       get_index_of_left_child,
                                       get_index_of_right_child,
                                       max_heapify)


@pytest.mark.parametrize("A, expected", [
    ([5, 2, 4, 6, 1, 3], [1, 2, 3, 4, 5, 6]),
    (["d", "j", "a", "z", "r"], ["a", "d", "j", "r", "z"]),
])
def test_insertion_sort(A, expected):
    # insertion_sort mutates the input sequence
    insertion_sort(A)
    assert A == expected


@pytest.mark.parametrize("i, expected", [
    (1, 0),
    (2, 0),
    (3, 1),
    (4, 1),
    (7, 3),
    (9, 4),
    (5, 2),
    (6, 2),
])
def test_heap_get_index_of_parent(i, expected):
    assert get_index_of_parent(i) == expected


@pytest.mark.parametrize("i, expected", [
    (0, 1),
    (1, 3),
    (2, 5),
    (3, 7),
    (2, 5),
    (4, 9),
])
def test_heap_get_index_of_left_child(i, expected):
    assert get_index_of_left_child(i) == expected


@pytest.mark.parametrize("i, expected", [
    (0, 2),
    (1, 4),
    (2, 6),
    (3, 8),
])
def test_heap_get_index_of_right_child(i, expected):
    assert get_index_of_right_child(i) == expected


@pytest.mark.parametrize("A, i, expected", [
    ([16, 4, 10, 14, 7, 9, 3, 2, 8, 1], 1, [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]),
    ([27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9], 2, [27, 17, 10, 16, 13, 9, 1, 5, 7, 12, 4, 8, 3])
])
def test_heap_max_heapify(A, i, expected):
    max_heapify(A, i)
    assert A == expected
