from __future__ import annotations
from collections.abc import Iterable
from typing import override
from .Element import Elem, Exponent, elem

class MutableWord:
    word : list[Elem]

    def __init__(self, elems : list[Elem]) -> None:
        self.word = elems

    def immutable(self) -> Word:
        return Word(tuple(self.word))

class Word:
    word : tuple[Elem, ...]
    length : int = 0
    
    def __init__(self, word : tuple[Elem, ...]) -> None:
        self.word = word
        for element in word:
            self.length += abs(element.exp)

    def reduced(self) -> Word:
        reducedWord : MutableWord = MutableWord([])
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
        return reducedWord.immutable()

    def concat(self, other: Word) -> Word:
        addedWord : MutableWord = MutableWord([])
        addedWord.word.extend(self.word)
        addedWord.word.extend(other.word)
        return addedWord.immutable()

    def __iter__(self) -> Iterable[Elem]:
        for i in self.word:
            yield i

    def __mul__(self, other: object) -> Word:
        if isinstance(other, Word):
            return self.concat(other).reduced()
        if isinstance(other, Elem):
            return self * Word((other,))
        else:
            return NotImplemented

    def __rmul__(self, other: object) -> Word:
        if isinstance(other, Word):
            return other.concat(self).reduced()
        if isinstance(other, Elem):
            return Word((other,)) * self
        else:
            return NotImplemented

    def __pow__(self, exp: Exponent) -> Word:
        if exp < 0:
            return (self ** -exp).inv()
        elif exp == 0:
            return Word(())
        else:
            newWord : MutableWord = MutableWord([])
            for _ in range(exp):
                newWord.word.extend(self.word)
            return newWord.immutable()


    def inv(self) -> Word:
        return MutableWord([Elem(element.sym, -1 * element.exp) for element in self.word[::-1]]).immutable()
    
    @override
    def __repr__(self) -> str:
        if self.length == 0:
            return "ε"
        return "".join([str(elem) for elem in self.word])

    def strictEquality(self, other : Word) -> bool:
        if (len(self.word) != len(other.word)):
            return False
        else:
            for i in range(len(self.word)):
                if self.word[i] != other.word[i]:
                    return False
            return True

    @override
    def __eq__(self, other: object, /) -> bool:
        return isinstance(other, Word) and self.reduced().strictEquality(other.reduced())

    @override
    def __hash__(self) -> int:
        return hash(self.word)

    def __len__(self) -> int:
        return self.length

def word(raw : str) -> Word:
    return Word(tuple([elem(i) for i in raw.split(" ")]))
