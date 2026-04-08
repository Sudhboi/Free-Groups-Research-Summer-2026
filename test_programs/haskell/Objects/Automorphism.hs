module Automorphism (
    Automorphism,
    mkAutomorphism,
    amap
)
where

import qualified Data.Map as M
import Element
import FreeGroup
import GroupWord
import ReducedWord
import Data.Group

data Automorphism = Automorphism { group :: FreeGroup,                           -- This is technically just a morphism, and depends on the user to
                                   mmap :: (M.Map Symbol RWord)} deriving (Show) -- supply an "auto"morphism.                                        

mkAutomorphism :: FreeGroup -> [(Symbol, RWord)] -> Automorphism
mkAutomorphism group mapList = Automorphism group (makeMap group mapList)

makeMap :: FreeGroup -> [(Symbol, RWord)] -> (M.Map Symbol RWord)
makeMap group mapList = foldl mapHelper M.empty (symbols group)
    where mapHelper currMap sym = M.insert sym (get sym) currMap
          get sym = case (lookup sym mapList) of
                            Just word -> word
                            Nothing -> elemRWord (Elem sym 1)

amap :: Automorphism -> GroupWord -> RWord
amap morph [] = RWord []
amap morph ((Elem sym expo):rest) = (pow (getWord sym) expo) <> (amap morph rest)   
    where getWord sym = (mmap morph) M.! sym
