from typing import Dict, List, Mapping, Set

explored: Set[str] = set([])
topological_order: Dict[str, int] = {}
current_label: int = 0


def topological_sort(g: Mapping[str, List[str]]) -> Dict[str, int]:
    """
    Return a linear ordering of a directed graph's vertices such that for every directed edge uv from vertex u to
    vertex v, u comes before v in the ordering (definition from wikipedia).

    :param dict g: graph represented as an adjacency list.
    :returns: dict of nodes as keys with values representing their topological ordering.
    """
    global explored
    global topological_order
    global current_label

    nodes = g.keys()
    explored = set([])
    current_label = len(g)  # count backwards
    topological_order = {}

    for node in nodes:
        if node not in explored:
            dfs(g, node)
        explored.add(node)
    return topological_order


def dfs(g: Mapping[str, List[str]], node: str):
    """
    Depth first search of a graph given a starting node that adds leaf or 'sink' nodes to topological_order as they
    are popped off the recursive stack.

    :param dict g: graph represented as an adjacency list.
    :param str node: string representing node in graph.
    """
    global explored
    global topological_order
    global current_label
    neighboring_nodes = g.get(node, None)
    if neighboring_nodes is None:
        return
    for neighbor in neighboring_nodes:
        if neighbor not in explored:
            explored.add(neighbor)
            dfs(g, neighbor)
    topological_order[node] = current_label
    current_label -= 1
