from __future__ import annotations
from typing import override
from .Element import *

class Word:
    word : list[Elem]
    
    def __init__(self, word : list[Elem]) -> None:
        self.word = word

    def reduced(self) -> Word:
        reducedWord : Word = Word([])
        for currElem in self.word:
            if len(reducedWord.word) == 0:
                reducedWord.word.append(currElem)
            elif currElem.exp != 0:
                prevElem = reducedWord.word[-1]
                if prevElem.sym == currElem.sym:
                    _ = reducedWord.word.pop()
                    toAdd = Elem(currElem.sym, prevElem.exp + currElem.exp)
                    if toAdd.exp != 0:
                        reducedWord.word.append(toAdd)
                else:
                    reducedWord.word.append(currElem)
        return reducedWord

    def concat(self, other: Word):
        addedWord : Word = Word([])
        addedWord.word.extend(self.word)
        addedWord.word.extend(other.word)
        return addedWord

    def __mul__(self, other: Word) -> Word:
        return self.concat(other).reduced()


    def inv(self) -> Word:
        return Word([Elem(element.sym, -1 * element.exp) for element in self.word[::-1]])
    
    @override
    def __repr__(self) -> str:
        return "".join([str(elem) for elem in self.word])

    def strictEquality(self, other : Word) -> bool:
        if (len(self.word) != len(other.word)):
            print("different length")
            return False
        else:
            for i in range(len(self.word)):
                if self.word[i] != other.word[i]:
                    return False
            return True

    @override
    def __eq__(self, other: object, /) -> bool:
        return isinstance(other, Word) and self.reduced().strictEquality(other.reduced())

def word(raw : str) -> Word:
    return Word([elem(i) for i in raw.split(" ")])
