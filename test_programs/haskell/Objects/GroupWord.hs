module GroupWord (
    GroupWord(..),
    reduceWord,
    readWord,
    (+:+),
    inv
)
where

import Data.Group
import Element

type GroupWord = [Elem]

reduceWord :: GroupWord -> GroupWord
reduceWord = reverse . (foldl reducer [])
reducer :: GroupWord -> Elem -> GroupWord

reducer list (Elem _ 0) = list
reducer [] ele = ele : []
reducer list@((Elem csym cexp) : xs) ele@(Elem asym aexp)
    | csym == asym = reducer xs (Elem csym (cexp + aexp))
    | otherwise = ele:list

readWord :: String -> GroupWord
readWord = map readRaw . words

(+:+) :: GroupWord -> GroupWord -> GroupWord
wordA +:+ wordB = reduceWord $ wordA ++ wordB

inv :: GroupWord -> GroupWord
inv = foldl invert []
    where invert list (Elem csym cexp) = Elem csym (-cexp) : list

