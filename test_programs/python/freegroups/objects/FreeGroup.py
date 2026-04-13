from .Word import *
from .Element import *
import random

class FreeGroup:

    basis : tuple[Symbol, ...]
    alphabet : tuple[Elem, ...]
    rank : int

    def __init__(self, basis : tuple[Symbol, ...]) -> None:
        self.basis = basis
        self.rank = len(basis)
        temp_alphabet : list[Elem] = []
        for sym in basis:
            temp_alphabet.extend([Elem(sym, power) for power in [-1, 1]])
        self.alphabet = tuple(temp_alphabet)


    def generate_to_length(self, length : int) -> list[Word]:
        word_list : list[Word] = [Word((e,)) for e in self.alphabet]
        for _ in range(length - 1):
            next_words : list[Word] = []
            for alph in self.alphabet:
                for word in word_list:
                    next_words.append(word * Word((alph,)))
            print(next_words)
            word_list.extend(next_words)
        return word_list

def getFreeGroup(rank : int) -> FreeGroup:
    basisList: list[str] = []
    for i in range(97, 97 + rank):
        basisList.append(chr(i))
    return FreeGroup(tuple(basisList))

def genRandWord(group : FreeGroup, length : int, variation : int) -> tuple[Word, int]:
    newWord = MutableWord([])
    prevSym: Symbol = ""
    count = 0
    while count <= length:
        sym: Symbol = group.basis[random.randint(0, group.rank - 1)]
        if sym == prevSym:
            continue
        prevSym = sym
        expo = 0 
        while expo == 0:
            expo = random.randint(-variation, variation)
        newWord.word.append(Elem(sym, expo))
        count += abs(expo)
    return (newWord.immutable(), count)

