from objects.Word import *

wordA : Word = Word([Elem("a", 2), Elem("b", 0), Elem("a", -1)])
wordB : Word = Word([Elem("a", 1)])
wordC : Word = word("a^2 b b^2 a^-1")

print(wordA)
print(wordA.reduced())
print(wordB.reduced())
print(Elem("A", 1) == Elem("A", 1))
print(wordA.reduced().strictEquality(wordB))
print(elem("a^2"))
print(wordC)
print(wordC.reduced())
print(wordC.reduced().inv())
print(wordC.reduced() * wordC.reduced().inv())
