import time
from objects.WhiteheadAutomorphism import generateType2WAMaps
from objects.FreeGroup import FreeGroup
from objects.Word import *

whiteheadList = generateType2WAMaps(FreeGroup(("a", "b")))
print("Done:")
for i in whiteheadList:
    print(i)
print(len(whiteheadList))

# k = word("a e^3 b^3 f^-13 c^4 f^17 d^-5")
# reduced = k.reduced()
#
# p = time.time()
# min_length = k.length
# length_changed = True
# while length_changed:
#     length_changed = False
#     for phi in whiteheadList:
#         new = phi.map(reduced)
#         if new.length < min_length:
#             print(new.length, new, phi.morphism_map)
#             min_length = new.length
#             reduced = new
#             length_changed = True
#             break
#
# print("Reduced in", time.time() - p)
# print("Given:", k)
# print("Minimal:", reduced)
