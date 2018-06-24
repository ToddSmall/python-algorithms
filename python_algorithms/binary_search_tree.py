"""Implementating a no-frills binary search tree."""

from abc import abstractmethod
from typing import Any, Generator, Optional, TypeVar
from typing_extensions import Protocol


class Comparable(Protocol):
    @abstractmethod
    def __lt__(self, other: Any):
        pass


CT = TypeVar("CT", bound=Comparable)

class TreeNode:
    def __init__(
        self,
        key: CT,
        value: Any,
        parent: Optional["TreeNode"] = None,
        left_child: Optional["TreeNode"] = None,
        right_child: Optional["TreeNode"] = None,
    ) -> None:
        self._key = key
        self._value = value
        self._parent = parent
        self._left_child = left_child
        self._right_child = right_child

    @property
    def key(self) -> CT:
        return self._key
    
    @property
    def parent(self) -> Optional["TreeNode"]:
        """Get the node's parent."""
        return self._parent

    @parent.setter
    def parent(self, tree_node: Optional["TreeNode"]) -> None:
        self._parent = tree_node

    @property
    def left_child(self) -> Optional["TreeNode"]:
        """Get the node's left child."""
        return self._left_child

    @left_child.setter
    def left_child(self, tree_node: Optional["TreeNode"]) -> None:
        self._left_child = tree_node

    @property
    def right_child(self) -> Optional["TreeNode"]:
        """Get the node's right child."""
        return self._right_child

    @right_child.setter
    def right_child(self, tree_node: Optional["TreeNode"]) -> None:
        self._right_child = tree_node


def tree_insert(root: TreeNode, new_node: TreeNode) -> None:
    """Insert `new_node` into the binary search tree with root `root`."""
    trailing_node: Optional["TreeNode"] = None
    x: Optional["TreeNode"] = root
    while x is not None:
        trailing_node = x
        if new_node.key < x.key:
            x = x.left_child
        else:
            x = x.right_child
    new_node.parent = trailing_node
    if trailing_node is not None:
        if new_node.key < trailing_node.key:
            trailing_node.left_child = new_node
        else:
            trailing_node.right_child = new_node


def in_order_tree_walk(node: Optional[TreeNode]) -> Generator[CT, None, None]:
    """Generate the ordered sequence of node keys."""
    if node is not None:
        yield from in_order_tree_walk(node.left_child)
        yield node.key
        yield from in_order_tree_walk(node.right_child)


def tree_search(node: Optional[TreeNode], key: CT) -> Optional[TreeNode]:
    """Search a binary search tree from `node` for the specified `key`."""
    if node is None or node.key == key:
        return node
    if key < node.key:
        return tree_search(node.left_child, key)
    return tree_search(node.right_child, key)


def tree_minimum(node: Optional[TreeNode]) -> Optional[TreeNode]:
    """Return the node with minimum key in the tree rooted at `node`."""
    if node is None:
        return None
    while node.left_child is not None:
        node = node.left_child
    return node
