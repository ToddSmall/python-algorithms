"""Tests of sorting algorithms implemented in Python."""

import pytest

from python_algorithms.sorting import (
    insertion_sort,
    get_index_of_parent,
    get_index_of_left_child,
    get_index_of_right_child,
    get_first_leaf_index,
    max_heapify,
    build_max_heap,
    heap_sort,
    partition,
    quick_sort,
    randomized_select
)


@pytest.mark.parametrize(
    "A, expected",
    [
        ([5, 2, 4, 6, 1, 3], [1, 2, 3, 4, 5, 6]),
        (["d", "j", "a", "z", "r"], ["a", "d", "j", "r", "z"]),
    ],
)
def test_insertion_sort(A, expected):
    # insertion_sort mutates the input sequence
    insertion_sort(A)
    assert A == expected


@pytest.mark.parametrize(
    "i, expected", [(1, 0), (2, 0), (3, 1), (4, 1), (7, 3), (9, 4), (5, 2), (6, 2)]
)
def test_heap_get_index_of_parent(i, expected):
    assert get_index_of_parent(i) == expected


@pytest.mark.parametrize(
    "i, expected", [(0, 1), (1, 3), (2, 5), (3, 7), (2, 5), (4, 9)]
)
def test_heap_get_index_of_left_child(i, expected):
    assert get_index_of_left_child(i) == expected


@pytest.mark.parametrize("i, expected", [(0, 2), (1, 4), (2, 6), (3, 8)])
def test_heap_get_index_of_right_child(i, expected):
    assert get_index_of_right_child(i) == expected


@pytest.mark.parametrize("len_heap, expected", [(10, 5), (13, 6)])
def test_get_first_leaf_index(len_heap, expected):
    assert get_first_leaf_index(len_heap) == expected


@pytest.mark.parametrize(
    "A, i, expected",
    [
        ([16, 4, 10, 14, 7, 9, 3, 2, 8, 1], 1, [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]),
        (
            [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9],
            2,
            [27, 17, 10, 16, 13, 9, 1, 5, 7, 12, 4, 8, 3],
        ),
    ],
)
def test_heap_max_heapify(A, i, expected):
    max_heapify(A, i)
    assert A == expected


@pytest.mark.parametrize(
    "A, expected",
    [
        ([4, 1, 3, 2, 16, 9, 10, 14, 8, 7], [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]),
        (
            [1, 10, 9, 5, 8, 17, 7, 4, 16, 3, 27, 13, 12],
            [27, 16, 17, 5, 10, 13, 7, 4, 1, 3, 8, 9, 12],
        ),
    ],
)
def test_build_max_heap(A, expected):
    build_max_heap(A)
    assert A == expected


@pytest.mark.parametrize(
    "A, expected",
    [
        ([4, 1, 3, 2, 16, 9, 10, 14, 8, 7], [1, 2, 3, 4, 7, 8, 9, 10, 14, 16]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([], []),
    ],
)
def test_heap_sort(A, expected):
    heap_sort(A)
    assert A == expected


@pytest.mark.parametrize(
    "A, p, r, q, expected",
    [
        ([2, 8, 7, 1, 3, 5, 6, 4], None, None, 3, [2, 1, 3, 4, 7, 5, 6, 8]),
        (
            [13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11],
            None,
            None,
            7,
            [9, 5, 8, 7, 4, 2, 6, 11, 21, 13, 19, 12],
        ),
    ],
)
def test_partition(A, p, r, q, expected):
    assert partition(A) == q
    assert A == expected


@pytest.mark.parametrize(
    "A, expected",
    [
        ([2, 8, 7, 1, 3, 5, 6, 4], [1, 2, 3, 4, 5, 6, 7, 8]),
        (
            [13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11],
            [2, 4, 5, 6, 7, 8, 9, 11, 12, 13, 19, 21],
        ),
        ([3, 4, 5, 6, 7], [3, 4, 5, 6, 7]),
        ([], []),
    ],
)
def test_quick_sort(A, expected):
    quick_sort(A)
    assert A == expected


@pytest.mark.parametrize("A, i, expected", [
    ([13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11], 5, 7),
    ([13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11], 7, 9),
    ([13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11], 100, 21) 
])
def test_randomized_select(A, i, expected):
    assert randomized_select(A, i) == expected