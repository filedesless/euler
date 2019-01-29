module P005(
  p005) where

import Data.List
import Data.Function( on )

p005 :: Int
p005 = product $ primes >>= \n -> filter (== n) . maxim . filter (elem n) $ facts
  where
    maxim = maximumBy (compare `on` length)
    facts = map factors [11..20]

factors :: Int -> [Int]
factors n
  | elem n primes = [n]
  | otherwise     = i : factors (div n i)
  where (i:_) = filter ((== 0) . mod n) primes

primes = [2,3,5,7,11,13,17,19]
