from .WhiteheadAutomorphism import *
import pickle
import time

def getWhiteheadFromCache(rank : int) -> list[Morphism]:
    readFile = open("../whiteheadcache/rank{}".format(rank), "rb+")
    group = getFreeGroup(rank)
    cTime = time.time()
    mapList: list[dict[Symbol, Word]] = pickle.load(readFile)
    print("Read File:", time.time() - cTime)
    nTime = time.time()
    morphList: list[Morphism] = []
    for i in mapList:
        morphList.append(Morphism(group, i))
    print("Create Objects:", time.time() - nTime)
    return morphList

def writeWhiteheadCache(rank : int) -> None:
    cTime = time.time()
    whiteHeadList = generateType2WAMaps(getFreeGroup(rank))
    print("Wrote Cache for rank {} in:".format(rank), time.time() - cTime)
    toFile = open("../whiteheadcache/rank{}".format(rank), "wb+")
    pickle.dump(whiteHeadList, toFile)
    toFile.close()
