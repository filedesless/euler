module P001(
  p001) where

p001 :: Int
p001 = sum [ i | i <- [0..999], mod i 5 == 0 || mod i 3 == 0 ]
