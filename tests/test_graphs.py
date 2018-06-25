import pytest

from python_algorithms.graphs import Graph, breadth_first_search, NodeColor


@pytest.fixture
def undirected_graph():
    connections = [
        ("r", "s", 1),
        ("r", "v", 1),
        ("s", "r", 1),
        ("s", "w", 1),
        ("t", "u", 1),
        ("t", "w", 1),
        ("t", "x", 1),
        ("u", "t", 1),
        ("u", "x", 1),
        ("u", "y", 1),
        ("v", "r", 1),
        ("w", "s", 1),
        ("w", "t", 1),
        ("w", "x", 1),
        ("x", "t", 1),
        ("x", "u", 1),
        ("x", "w", 1),
        ("x", "y", 1),
        ("y", "u", 1),
        ("y", "x", 1),
    ]
    return Graph(connections)


def test_build_graph(undirected_graph):
    vertices = undirected_graph.vertices
    assert vertices.keys() == {"r", "s", "t", "u", "v", "w", "x", "y"}
    assert vertices["r"].neighbors == {vertices["s"]: 1, vertices["v"]: 1}
    assert vertices["v"].neighbors == {vertices["r"]: 1}
    assert vertices["x"].neighbors == {
        vertices["t"]: 1,
        vertices["u"]: 1,
        vertices["w"]: 1,
        vertices["y"]: 1,
    }


def test_breadth_first_search(undirected_graph):
    vertices = undirected_graph.vertices
    breadth_first_search(undirected_graph, undirected_graph.vertices["s"])

    assert all((v.color == NodeColor.BLACK) for v in vertices.values())

    assert vertices["s"].distance == 0
    assert vertices["s"].predecessor is None
    assert vertices["r"].distance == 1
    assert vertices["r"].predecessor == vertices["s"]
    assert vertices["v"].distance == 2
    assert vertices["v"].predecessor == vertices["r"]
    assert vertices["t"].distance == 2
    assert vertices["t"].predecessor == vertices["w"]
    assert vertices["y"].distance == 3
    assert vertices["y"].predecessor == vertices["x"]
