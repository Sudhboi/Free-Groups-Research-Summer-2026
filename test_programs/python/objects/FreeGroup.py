from .Word import *
from .Element import *

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
            word_list.extend(next_words)
        return word_list

