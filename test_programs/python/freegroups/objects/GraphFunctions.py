from graph_tool.all import Graph, min_cut, graph_draw
from .Element import Elem

def create_partitions(wh_graph : Graph) -> tuple[set[Elem], set[Elem]]:
    weight = wh_graph.edge_properties["weight"]
    elem = wh_graph.vertex_properties["elem"]
    mc, part = min_cut(wh_graph, weight)
    part1 = set()
    part2 = set()
    for v in wh_graph.vertices():
        (part1 if part[v] else part2).add(elem[v])
    return (part1, part2)
