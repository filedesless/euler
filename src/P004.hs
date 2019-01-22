module P004(
  p004) where

p004 :: Int
p004 = maximum $ filter (isPalindrome . show) products

isPalindrome :: Eq a => [a] -> Bool
isPalindrome [ ] = True
isPalindrome [a] = True
isPalindrome (h:t)
  | h == last t = isPalindrome $ init t
  | otherwise = False

products :: [Int]
products = [ x * y | x <- [100..999], y <- [100..999] ]
