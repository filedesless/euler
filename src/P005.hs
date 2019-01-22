module P005(
  p005) where

p005 :: Int
p005 = head $ filter divisible [11,22..]

divisible :: Int -> Bool
divisible n = all (\i -> mod n i == 0) [20, 19..12]
