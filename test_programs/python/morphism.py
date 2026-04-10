from objects import *

nielsen : list[Morphism] = []
groupA : FreeGroup = FreeGroup(("a", "b", "c"))
for sym in groupA.basis:
    for other in groupA.basis:
        if sym != other:
            nielsen.extend([Morphism(groupA, {sym : Word((Elem(sym, 1), Elem(other, i)))}) for i in [-1, 1]])
            nielsen.extend([Morphism(groupA, {sym : Word((Elem(other, i), Elem(sym, 1)))}) for i in [-1, 1]])

k = word("a b^3 a^-1 a b^-3 a b^3 a^-1 a b^-3 a b^3 a^-1 a b^-3 a b^3 a^-1 a b^-3")
reduced = k

min_length = k.length
length_changed = True
while length_changed:
    length_changed = False
    for phi in nielsen:
        new = phi.map(reduced)
        if new.length < min_length:
            print(new.length, new, phi.morphism_map)
            min_length = new.length
            reduced = new
            length_changed = True

print("Given:", k)
print("Minimal:", reduced)
