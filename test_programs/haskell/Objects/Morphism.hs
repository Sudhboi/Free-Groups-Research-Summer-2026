module Morphism (
    Morphism,
    mkMorphism,
    amap,
)
where

import Data.Group
import Data.Map qualified as M
import Element
import FreeGroup
import GroupWord
import ReducedWord

data Morphism = Morphism
    { group :: FreeGroup
    , mmap :: M.Map Symbol RWord
    }
    deriving (Show)

mkMorphism :: FreeGroup -> [(Symbol, RWord)] -> Morphism
mkMorphism group mapList = Morphism group (makeMap group mapList)

makeMap :: FreeGroup -> [(Symbol, RWord)] -> M.Map Symbol RWord
makeMap group mapList = foldl mapHelper M.empty (symbols group)
  where
    mapHelper currMap sym = M.insert sym (get sym) currMap
    get sym = case lookup sym mapList of
        Just word -> word
        Nothing -> elemRWord (Elem sym 1)

amap :: Morphism -> GroupWord -> RWord
amap morph [] = RWord []
amap morph ((Elem sym expo) : rest) = pow (getWord sym) expo <> amap morph rest
  where
    getWord sym = mmap morph M.! sym
