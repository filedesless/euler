module P002(
  p002) where

p002 :: Int
p002 = sum $ filter even $ takeWhile (< 4000000) fibo

fibo :: [Int]
fibo = 1 : 2 : [ a + b | (a, b) <- zip fibo (tail fibo) ]
