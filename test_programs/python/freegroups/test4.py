from objects import getFreeGroup, getWhiteheadFromCache, word, genRandWord
import time

rank = 7
grp = getFreeGroup(rank)
whiteheadList = getWhiteheadFromCache(rank)
# w, l = genRandWord(grp, 20, 3)
# print(w.get_copyable())
w = word("e^4 f^-1 e^20 f^-15 c^19 d^13 e^3 c^18 f^11 c^-18 b^11 a^-8 f^2 b^-15 e^-11 d^14 b^-1 d^16 g^-19 d^-2 f^9 a^-1 d^7 e^1 a^-2 d^-14 f^17 b^-2 a^11 e^-14 f^11 b^20 d^19 a^-7 f^5 b^-10 e^-8 f^-4 a^2 e^19 f^16 b^-18 e^-16 b^-3 f^20 d^8 g^-16 f^-11 e^-18 b^-11 a^15 d^-11 b^-1 e^15 c^-10 e^-12 b^5 a^-5 d^-12 c^6 b^4 c^12 b^12 e^13 c^8 b^-2 d^19 a^-11 b^9 c^-6 a^-14 d^15 f^-3 e^9 f^-5 a^-12 f^8 a^6 e^2 f^-19 c^-8 e^-10 a^-6 f^-13 c^-14 d^-5 f^8 e^-1 a^-20 f^13 c^2 f^-20 a^-14 f^15 a^-10 g^-7 d^-4 b^18")
k = [(w, w.length)]

for rword, length in k:
    print("Given:", rword, length)

    reduced = rword.reduced()

    p = time.time()
    min_length = reduced.length
    length_changed = True
    while length_changed:
        length_changed = False
        for phi in whiteheadList:
            new = phi.map(reduced)
            if new.length < min_length:
                print(phi.morphism_map)
                min_length = new.length
                reduced = new
                length_changed = True
                break

    print("Minimized in", time.time() - p)
    print("Minimal:", reduced, min_length, "Diff:", "\033[1;31m", length - min_length, "\033[0m")
