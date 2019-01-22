module P006(
  p006) where

p006 :: Int
p006 = x - y
  where
    x = sum [1..100] ^ 2
    y = sum $ map (^ 2) [1..100]
