"""Noodling with graph algorithms."""

from collections import deque
from enum import Enum
import sys
from typing import Dict, Iterable, Optional, Set, Tuple


class NodeColor(Enum):
    WHITE = 1
    GRAY = 2
    BLACK = 3


class Vertex:
    def __init__(
        self,
        label: str,
        neighbors: Optional[Dict["Vertex", float]] = None,
        color: Optional[NodeColor] = None,
        distance: Optional[float] = None,
        predecessor: Optional["Vertex"] = None,
    ) -> None:
        self._label = label
        self._neighbors = neighbors
        self._color = color
        self._distance = distance
        self._predecessor = predecessor

    def __str__(self) -> str:
        """Return an easy-to-read description of the vertex."""
        if self._neighbors is None:
            return f"vertex {self._label}, has no neighbors"
        neighbors = ', '.join([v.label for v in self._neighbors])
        return f"vertex {self._label}, connected to {neighbors}"

    @property
    def label(self) -> str:
        """Get the node's `label`."""
        return self._label

    @property
    def neighbors(self) -> Optional[Dict["Vertex", float]]:
        """Get the node's neighbors."""
        return self._neighbors

    @property
    def color(self) -> Optional[NodeColor]:
        """Get the node's color."""
        return self._color

    @color.setter
    def color(self, value: NodeColor) -> None:
        self._color = value

    @property
    def distance(self) -> Optional[float]:
        """Get the node's distance from the origin."""
        return self._distance

    @distance.setter
    def distance(self, value: float) -> None:
        self._distance = value

    @property
    def predecessor(self) -> Optional["Vertex"]:
        """Get the node's predecessor in the graph."""
        return self._predecessor

    @predecessor.setter
    def predecessor(self, value: Optional["Vertex"]) -> None:
        self._predecessor = value

    def add_neighbor(self, neighbor: "Vertex", edge_weight: float) -> None:
        if self._neighbors is None:
            self._neighbors = dict()
        self._neighbors[neighbor] = edge_weight


class Graph:
    def __init__(self, connections: Iterable[Tuple[str, str, float]]) -> None:
        self._build_graph(connections)

    @property
    def vertices(self) -> Dict[str, Vertex]:
        return self._vertices

    def _build_graph(self, connections: Iterable[Tuple[str, str, float]]) -> None:
        self._vertices: Dict[str, Vertex] = dict()
        for first_label, second_label, edge_weight in connections:
            if first_label not in self._vertices:
                self._vertices[first_label] = Vertex(first_label)
            if second_label not in self._vertices:
                self._vertices[second_label] = Vertex(second_label)
            self._vertices[first_label].add_neighbor(self._vertices[second_label], edge_weight)


def breadth_first_search(graph: Graph, origin: Vertex) -> None:
    """Breadth-first search of `graph` starting from `origin`."""
    for v in graph.vertices.values():
        if v != origin:
            v.color = NodeColor.WHITE
            v.distance = sys.maxsize
            v.predecessor = None

    origin.color = NodeColor.GRAY
    origin.distance = 0
    origin.predecessor = None

    Q: deque = deque()
    Q.append(origin)

    while Q:
        u = Q.popleft()
        for v in u.neighbors:
            if v.color == NodeColor.WHITE:
                v.color = NodeColor.GRAY
                v.distance = u.distance + 1
                v.predecessor = u
                Q.append(v)
        u.color = NodeColor.BLACK

