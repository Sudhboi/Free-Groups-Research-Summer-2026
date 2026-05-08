import graph_tool.all as gt 
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
    inv_vertex = ug.new_vertex_property("int")
    for v in ug.vertices():
        elements[v] = lookup_inv[int(v)]
        inv_vertex[v] = lookup[elements[v].inv()]
    ug.vp["elem"] = elements
    ug.vp["inv_vertex"] = inv_vertex

    return ug

def draw_whitehead_graph(wh_graph : gt.Graph, output = None, part=None) -> None:
    weight = wh_graph.edge_properties["weight"]
    elem = wh_graph.vertex_properties["elem"]
    v_text = wh_graph.new_vertex_property("string")
    for v in wh_graph.vertices():
        v_text[v] = str(elem[v])
    graph_draw(wh_graph, edge_text=weight, vertex_text=v_text, output=output, vertex_fill_color=part)

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
        if abs(curr.exp) - 1 != 0:
            edge_list.append((lookup[curr_simp], 
                              lookup[curr_simp.inv()], 
                              abs(curr.exp) - 1))
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

def make_directed(whg : gt.Graph) -> gt.Graph:
    d_whg = gt.Graph(whg)
    d_whg.set_directed(True)
    d_whg.clear_edges()
    weight = whg.ep["weight"]
    rev_edge_list = []
    new_weight = d_whg.new_ep("int")
    for e in whg.iter_edges(eprops=[weight]):
        rev_edge_list.append((e[0], e[1], e[2]))
        rev_edge_list.append((e[1], e[0], e[2]))
    d_whg.add_edge_list(rev_edge_list, eprops = [new_weight])
    d_whg.ep["weight"] = new_weight
    return d_whg

def find_partitions(g : gt.Graph) -> list[tuple[set[Elem], set[Elem]]]:
    dg = make_directed(g)
    cap = dg.ep["weight"]
    elem = dg.vp["elem"]
    inv = dg.vp["inv_vertex"]
    partitions : list[tuple[set[Elem], set[Elem]]] = []
    for src in dg.vertices():
        tgt = dg.vertex(inv[src])
        cap = dg.ep["weight"]
        res = gt.boykov_kolmogorov_max_flow(dg, src, tgt, cap)
        part = gt.min_st_cut(dg, src, cap, res)
        temp = [cap[e] for e in dg.edges() if part[e.source()] != part[e.target()]]
        mc = sum(temp)//2
        # print(elem[src], "Degree:", src.out_degree(cap), "MinCut:", mc)
        # print(temp)
        if mc < src.out_degree(cap):
            draw_whitehead_graph(dg, part=part)
            part1 = set()
            part2 = set()
            for v in dg.vertices():
                (part1 if part[v] else part2).add(elem[v])
            partitions.append((part1, part2))
    return clean_partitions(partitions)

def clean_partitions(partlist : list[tuple[set[Elem], set[Elem]]]) -> list[tuple[set[Elem], set[Elem]]]:
    non_duplicate : list[tuple[set[Elem], set[Elem]]] = []
    for parts in partlist:
        if not (parts in non_duplicate or parts[::-1] in non_duplicate):
            non_duplicate.append(parts)
    return non_duplicate
