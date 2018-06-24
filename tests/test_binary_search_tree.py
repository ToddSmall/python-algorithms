import pytest

from python_algorithms.binary_search_tree import (
    TreeNode,
    tree_insert,
    in_order_tree_walk,
    tree_search,
    tree_minimum,
)

SOME_INTEGERS = [15, 6, 18, 3, 7, 17, 20, 2, 4, 13, 9]

def test_build_a_tree():
    root = TreeNode(key=12, value=None)
    five_node = TreeNode(key=5, value=None)
    tree_insert(root, five_node)
    assert root.left_child == five_node
    assert root.right_child is None
    assert five_node.parent == root

    two_node = TreeNode(key=2, value=None)
    tree_insert(root, two_node)
    assert two_node.parent == five_node
    assert five_node.left_child == two_node
    assert five_node.right_child is None

    nine_node = TreeNode(key=9, value=None)
    tree_insert(root, nine_node)
    assert nine_node.parent == five_node
    assert five_node.left_child == two_node
    assert five_node.right_child == nine_node

    eightteen_node = TreeNode(key=18, value=None)
    tree_insert(root, eightteen_node)
    assert eightteen_node.parent == root
    assert root.left_child == five_node
    assert root.right_child == eightteen_node

    fifteen_node = TreeNode(key=15, value=None)
    tree_insert(root, fifteen_node)
    assert fifteen_node.parent == eightteen_node
    assert eightteen_node.left_child == fifteen_node
    assert eightteen_node.right_child is None


@pytest.fixture
def tree_root():
    root = TreeNode(key=SOME_INTEGERS[0], value=None)
    for key in SOME_INTEGERS[1:]:
        tree_insert(root, TreeNode(key=key, value=None))
    return root


def test_in_order_tree_walk(tree_root):
    sorted_keys = list(in_order_tree_walk(tree_root))
    assert sorted_keys == sorted(SOME_INTEGERS)


def test_tree_search(tree_root):
    computed = tree_search(tree_root, 99)
    assert computed is None

    computed = tree_search(tree_root, 17)
    assert computed.key == 17

    computed = tree_search(tree_root, tree_root.key)
    assert computed.key == tree_root.key


def test_tree_minimum(tree_root):
    computed = tree_minimum(tree_root)
    assert computed.key == min(SOME_INTEGERS)

    computed = tree_minimum(tree_root.right_child)
    assert computed.key == 17

    computed = tree_minimum(None)
    assert computed is None