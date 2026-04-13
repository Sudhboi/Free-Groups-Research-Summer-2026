from .FreeGroup import *

class Morphism:
    morphism_map : dict[Symbol, Word]
    free_group : FreeGroup

    def __init__(self, group : FreeGroup, map : dict[Symbol, Word]) -> None:
        self.free_group = group
        for sym in group.basis:
            if sym not in map:
                map[sym] = Word((Elem(sym, 1),))
        self.morphism_map = map

    def map(self, word : Word) -> Word:
        newWord = MutableWord([])
        for elem in word.word:
            newWord.word.extend((self.morphism_map[elem.sym] ** elem.exp).word)
        return newWord.immutable().reduced()


