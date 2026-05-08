from .WhiteheadAutomorphism import Morphism, generate_wh_automorphism
from .WhiteheadGraph import make_whitehead_graph, find_partitions
from .FreeGroup import FreeGroup
from .Element import Elem
from .Word import Word

def test_wh_automorphisms(partlist : list[tuple[set[Elem], set[Elem]]], w : Word, fg : FreeGroup):
    for p1, p2 in partlist:
        for A in [p1, p2]:
            for x in A:
                phi = generate_wh_automorphism(x, A, fg)
                nw = phi.map(w)
                if nw.length < w.length:
                    return phi, nw
    assert True, "This should not be happening"
    return (Morphism(fg, {}), w)

def minimize(gw : Word, fg : FreeGroup, show_trace : bool = False, show_graphs : bool = False) -> Word:
    w = gw
    if show_trace: 
        print(w.length, w)
    reduced = False
    while not reduced:
        g = make_whitehead_graph(w)
        partlist = find_partitions(g, draw_graph=show_graphs)
        if partlist != []:
            phi, nw = test_wh_automorphisms(partlist, w, fg)
            if show_trace:
                print(phi.morphism_map)
                print(nw.length, nw)
            w = nw
        else:
            reduced = True
    return w
