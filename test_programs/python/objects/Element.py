from typing import override

format_map = {0: "⁰", 1:"¹", 2: "²", 3: "³"}
for i in range(4, 10):
    format_map[i] = chr(0x2070 + i)

use_unicode : bool = True

type Symbol = str
type Exponent = int

class Elem:
    def __init__(self, symbol : Symbol, exponent : Exponent) -> None:
        self.sym : Symbol = symbol
        self.exp : Exponent = exponent

    @override
    def __eq__(self, other : object) -> bool:
        if not isinstance(other, Elem):
            return NotImplemented
        return self.sym == other.sym and self.exp == other.exp

    @override
    def __repr__(self) -> str:
        if use_unicode:
            if self.exp == 1:
                return self.sym
            elif self.exp >= 0 and self.exp < 10:
                return "{}{}".format(self.sym, format_map[self.exp])
            elif self.exp > -10:
                return "{}⁻{}".format(self.sym, format_map[-self.exp])
        return "{}^{}".format(self.sym, self.exp)

    @override
    def __hash__(self) -> int:
        return hash((self.sym, self.exp))

    # def __mul__(self, other : object) -> Word:
    #     if isinstance(other, Word):
    #         return Word((self,)) * other
    #     if isinstance(other, Elem):
    #         return Word((self,)) * Word((other,))
    #     else:
    #         return NotImplemented

def elem(raw: str) -> Elem:
    splits = raw.split("^") 
    if len(splits) == 1:
        return Elem(splits[0], 1)
    return Elem(splits[0], int(splits[1]))
