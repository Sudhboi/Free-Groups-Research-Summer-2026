from objects import *

rank = 4
grp = getFreeGroup(rank)
whiteheadList = getWhiteheadFromCache(rank)
w = word("a b^2")

k = [(w, 3)]

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
