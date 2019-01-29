module P010(
  p010) where

import P003( primes )

p010 :: Int
p010 = sum $ takeWhile (< 2000000) primes
