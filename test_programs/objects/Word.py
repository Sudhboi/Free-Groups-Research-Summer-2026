from __future__ import annotations
from typing import override
from .Element import *

class Word:
    word : list[Elem]
    
    def __init__(self, word : list[Elem]) -> None:
        self.word = word

    def reduced(self) -> Word:
        reducedWord : Word = Word(self.word[:])
        newWord : Word = Word([])

        if reducedWord.word != []:
            reduced : bool = True
            reducedInPrevCycle : bool = False
            while reduced:
                reduced = False
                for index in range(len(reducedWord.word) - 1):

                    if reducedInPrevCycle:
                        reducedInPrevCycle = False
                        continue

                    currentSym : Symbol = reducedWord.word[index].sym

                    if currentSym == reducedWord.word[index + 1].sym:
                        newWord.word.append(Elem(
                            symbol = currentSym, 
                            exponent = reducedWord.word[index].exp + reducedWord.word[index + 1].exp
                        ))
                        reduced = True
                        reducedInPrevCycle = True
                    elif reducedWord.word[index].exp == 0:
                        reduced = True
                    else:
                        newWord.word.append(reducedWord.word[index])

                if not reducedInPrevCycle:
                    lastElem : Elem = reducedWord.word[::-1][0]
                    if lastElem.exp != 0:
                        newWord.word.append(lastElem)
                
                reducedWord = newWord if newWord.word != [] else reducedWord
                newWord = Word([])

        if len(reducedWord.word) == 1 and reducedWord.word[0].exp == 0:
            return Word([])
        return reducedWord

    def __mul__(self, other: Word) -> Word:
        addedWord : Word = Word([])
        addedWord.word.extend(self.word)
        addedWord.word.extend(other.word)
        return addedWord.reduced()

    def inv(self) -> Word:
        return Word([Elem(element.sym, -1 * element.exp) for element in self.word[::-1]])
    
    @override
    def __repr__(self) -> str:
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

def word(raw : str) -> Word:
    return Word([elem(i) for i in raw.split(" ")])
