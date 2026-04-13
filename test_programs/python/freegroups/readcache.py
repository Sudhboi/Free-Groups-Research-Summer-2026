import pickle
from objects import *
import time

n = 4
readFile = open("whiteheadcache/rank{}".format(n), "rb+")
group = getFreeGroup(n)
cTime = time.time()
mapList: list[dict[Symbol, Word]] = pickle.load(readFile)
print("Done Reading!", time.time() - cTime)
nTime = time.time()
morphList: list[Morphism] = []
for i in mapList:
    morphList.append(Morphism(group, i))
print("Done Making!", time.time() - nTime)
print(len(morphList))
