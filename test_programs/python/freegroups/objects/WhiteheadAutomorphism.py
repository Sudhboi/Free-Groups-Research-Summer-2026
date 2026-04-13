"""
    1. Create the power set of the letters (L) in a free group.
    2. Iterate through all the subsets (called A) and do the following.
        a. Iterate through the letters (called x) in A.
        b. If x' is in SS:
            i. gg go next.
           Else:
            i. Define a morphism with the following map, iterating through all y in L.
            if y in A, y' not in A, and y not in {x, x'} : (A, x) y = yx
            if y not in A, y' in A, y not in {x, x'} : (A, x) y = x'y
            if both y, y' in A : (A, x) y = x'yx
            else : (A, x) y = y (do not need to add to the morphism map).

Piecewise definition taken from Virnig, 1998.
"""

from .Morphism import *
from .Powerset import powerset

def generateType2WAMaps(group : FreeGroup) -> list[dict[Symbol, Word]]:
    morphList : list[dict[Symbol, Word]] = []
    L = group.alphabet
    for A in powerset(L):
        for x in A:
            if x.inv() in A:
                continue
            phiMap: dict[Symbol, Word] = {}
            for ysym in group.basis:
                y = Elem(ysym, 1)
                if y in A and y.inv() not in A and y not in [x, x.inv()]:
                    phiMap[ysym] = Word((y, x))
                elif y.inv() in A and y not in A and y not in [x, x.inv()]:
                    phiMap[ysym] = Word((x.inv(), y))
                elif y in A and y.inv() in A:
                    phiMap[ysym] = Word((x.inv(), y, x))
            if phiMap != {}:
                morphList.append(phiMap)
    return morphList



