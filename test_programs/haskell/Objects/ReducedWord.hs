module ReducedWord
(   RWord(..),
    readRWord,
    reduce,
)
where

import Data.Group
import GroupWord

data RWord = RWord GroupWord deriving (Eq)

instance Show RWord where
    show (RWord word) = "ர " ++ (show word)

readRWord :: String -> RWord
readRWord str = RWord ((reduceWord . readWord) str)

reduce :: GroupWord -> RWord
reduce word = RWord (reduceWord word) 

instance Semigroup RWord where
    RWord a <> RWord b = RWord(a +:+ b)

instance Monoid RWord where
    mempty = RWord []

instance Group RWord where
    invert (RWord a) = RWord (inv a)
