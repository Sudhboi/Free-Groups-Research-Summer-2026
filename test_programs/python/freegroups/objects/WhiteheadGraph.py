import graph_tool as gt 
from graph_tool.draw import radial_tree_layout, graph_draw
from .Element import Elem
from .Word import Word

def make_whitehead_graph(word : Word) -> gt.Graph:
    ug = gt.Graph(directed=False)
    lookup, edge_list = get_edge_list(word)

    lookup_inv : dict[int, Elem] = {}
    for elem in lookup:
        lookup_inv[lookup[elem]] = elem 

    weight = ug.new_edge_property("int")
    ug.ep["weight"] = weight
    ug.add_edge_list(edge_list, eprops=[weight])

    elements = ug.new_vertex_property("object")
    for v in ug.vertices():
        elements[v] = lookup_inv[int(v)]
    ug.vp["elem"] = elements

    return ug

def draw_whitehead_graph(wh_graph : gt.Graph, output = None) -> None:
    weight = wh_graph.edge_properties["weight"]
    elem = wh_graph.vertex_properties["elem"]
    v_text = wh_graph.new_vertex_property("string")
    for v in wh_graph.vertices():
        v_text[v] = str(elem[v])
    print(elem)
    graph_draw(wh_graph, edge_text=weight, vertex_text=v_text, output=output)

def sgn(a : int) -> int:
    assert (a != 0)
    return 1 if a >= 1 else -1

def get_simple(elem: Elem) -> Elem:
    return Elem(elem.sym, sgn(elem.exp))

def get_edge_list(word: Word) -> tuple[dict[Elem, int], list[tuple[int, int, int]]]:
    cyclic_list : list[Elem] = list(word.word) + [word.word[0]]
    edge_list : list[tuple[int, int, int]] = []
    lookup : dict[Elem, int] = {}
    for i in range(len(cyclic_list) - 1):
        curr = cyclic_list[i]
        next = cyclic_list[i + 1]
        curr_simp = get_simple(curr)
        next_simp = get_simple(next)
        for elem in [curr_simp, curr_simp.inv(), next_simp.inv()]:
            if elem not in lookup:
                lookup[elem] = len(lookup)
        if curr.exp - 1 > 0:
            edge_list.append((lookup[curr_simp], 
                              lookup[curr_simp.inv()], 
                              curr.exp - 1))
        edge_list.append((lookup[curr_simp], lookup[next_simp.inv()], 1))
    return (lookup, clean_edge_list(edge_list))

def clean_edge_list(edge_list : list[tuple[int, int, int]]) -> list[tuple[int, int, int]]:
    cache : dict[tuple[int, int], int] = {}
    new_list : list[tuple[int, int, int]] = []
    for triple in edge_list:
        pair = (triple[0], triple[1])
        revpair = (triple[1], triple[0])
        if pair in cache:
            cache[pair] += triple[2]
        elif revpair in cache:
            cache[revpair] += triple[2]
        else:
            cache[pair] = triple[2]
    for pair in cache:
        new_list.append((pair[0], pair[1], cache[pair]))
    return new_list
