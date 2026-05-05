module ReducedWord (
    RWord (..),
    readRWord,
    reduce,
    elemRWord,
)
where

import Data.Group
import Element
import GroupWord

newtype RWord = RWord {groupWord :: GroupWord} deriving (Eq)

instance Show RWord where
    show (RWord word) = "r" ++ show word

instance Ord RWord where
    RWord wordA `compare` RWord wordB = (length wordA `compare` length wordB) <> (wordA `compare` wordB)

readRWord :: String -> RWord
readRWord str = RWord ((reduceWord . readWord) str)

elemRWord :: Elem -> RWord
elemRWord = RWord . elemWord

reduce :: GroupWord -> RWord
reduce word = RWord (reduceWord word)

instance Semigroup RWord where
    RWord a <> RWord b = RWord (a +:+ b)

instance Monoid RWord where
    mempty = RWord []

instance Group RWord where
    invert (RWord a) = RWord (inv a)
