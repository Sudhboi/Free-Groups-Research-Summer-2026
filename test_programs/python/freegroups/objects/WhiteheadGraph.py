import graph_tool as gt 
from .Word import Word
from .FreeGroup import FreeGroup

def make_whitehead_graph(word : Word, fg: FreeGroup) -> gt.Graph:
    g = gt.Graph(directed=False)
    
    return g
