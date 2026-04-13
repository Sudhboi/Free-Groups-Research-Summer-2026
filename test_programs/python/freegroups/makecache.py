import pickle
import time
from objects.WhiteheadAutomorphism import *

for n in range(8, 11):
    basisList: list[str] = []
    for i in range(97, 97 + n):
        basisList.append(chr(i))
    cTime = time.time()
    whiteHeadList = generateType2WAMaps(FreeGroup(tuple(basisList)))
    print("FreeGroupMaps of rank {}:".format(n), time.time() - cTime)
    toFile = open("whiteheadcache/rank{}".format(n), "wb+")
    pickle.dump(whiteHeadList, toFile)
    toFile.close()
