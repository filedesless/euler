module P009(
  p009) where

p009 :: Int
p009 = product triplet
  where (triplet:_) = [ [a, b, c] | a <- [0..999], b <- [a+1..999], c <- [b+1..999],
                        a + b + c == 1000, a*a + b*b == c*c ]
