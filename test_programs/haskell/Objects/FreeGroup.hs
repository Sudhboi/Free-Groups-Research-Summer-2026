module FreeGroup 
(   FreeGroup(..),
    getUniqueList,
    getElemsUpto,
    getElemsLength,
    mapAlph,
    getAlphElem,
    getAlph
)
where

import ReducedWord
import Element
import GroupWord

import qualified Data.Set as Set

data FreeGroup = FreeGroup { symbols :: [Symbol] } deriving (Show)

getUniqueList :: [RWord] -> [RWord]
getUniqueList = Set.toList . Set.fromList

getElemsLength :: FreeGroup -> Int -> [RWord]
getElemsLength group 1  = getUniqueList $ getAlph group 
getElemsLength group n  = getUniqueList $ mapAlph group <*> (getElemsLength group (n - 1))

getElemsUpto :: FreeGroup -> Int -> [RWord]
getElemsUpto group n = getUniqueList $ concat $ map (getElemsLength group) [1..n]

mapAlph :: FreeGroup -> [(RWord -> RWord)]
mapAlph = map (<>) . getAlph

getAlph :: FreeGroup -> [RWord]
getAlph = map elemRWord . getAlphElem 

getAlphElem :: FreeGroup -> [Elem]
getAlphElem = (foldr addElem []) . symbols
    where addElem rSym list = map (Elem rSym) [-1, 1]  ++ list
