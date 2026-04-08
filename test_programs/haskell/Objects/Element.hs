module Element 
(   Symbol,
    Exponent,
    Elem(..),
    readRaw
)
where

import Data.Strings
import Data.Char

type Symbol = [Char]
type Exponent = Int 

data Elem = Elem {sym :: Symbol, expo :: Exponent} deriving (Eq)

instance Ord Elem where
    (Elem asym aexpo) `compare` (Elem bsym bexpo) = (asym `compare` bsym) <> (aexpo `compare` bexpo)

instance Show Elem where
    show = pretty

pretty (Elem sym exp)
  | exp == 1 = sym
  | otherwise = sym ++ (superScript . show) exp

supers = [('-', '⁻'), ('0', '⁰'), ('1', '¹'), ('2', '²'), 
          ('3', '³'), ('4', '⁴'), ('5', '⁵'), ('6', '⁶'), 
          ('7', '⁷'), ('8', '⁸'), ('9', '⁹')]

superScript :: String -> String
superScript (x:xs) = case lookup x supers of
                          Just val -> val:(superScript xs)
superScript _ = ""

instance Read Elem where
    readsPrec _ = readElem

readElem :: String -> [(Elem, String)]
readElem str = case (strSplit "^" str) of 
                    (sym, rest) -> case expo of
                                   ""   -> [(Elem sym 1, "")]
                                   nums -> [(Elem sym (read nums), rester)]
                      where (expo, rester) = span (or . sequenceA [isDigit, ('-'==)]) rest

readRaw :: String -> Elem
readRaw str = case expo of "" -> Elem sym 1
                           other -> Elem sym (read other)
    where (sym, expo) = strSplit "^" str
