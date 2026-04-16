from objects.FreeGroup import *
from graph_tool.all import Graph, graph_draw

def sgn(x : int) -> int:
    if x == 0: return 0
    else: return int(abs(x)/x)

def make_whitehead_pairs(group : FreeGroup, word : Word) -> list[tuple[int, int]]:
    pairs : list[tuple[int, int]] = []
    indices = group.alphabet
    for i in range(len(word.word)):
        currElem = word.word[i]
        nextIndex = 0 if i == len(word.word) - 1 else i + 1
        nextElem = word.word[nextIndex]
        pairs.append((indices.index(Elem(nextElem.sym, sgn(nextElem.exp))), indices.index(Elem(currElem.sym, -sgn(currElem.exp)))))
    return pairs

def make_whitehead_graph(group : FreeGroup, word : Word) -> Graph:
    g : Graph = Graph(directed = False)
    g.add_edge_list([(i,) for i in group.alphabet], hashed=True, hash_type="object")
    g.add_edge_list(make_whitehead_pairs(group, word))
    return g

def draw_whitehead_graph(fg: FreeGroup, w: Word) -> None:
    g = make_whitehead_graph(fg, w)
    v_text = g.new_vertex_property("string")
    for v in g.vertices():
        v_text[v] = str(fg.alphabet[int(v)])
    graph_draw(g, vertex_text=v_text)
