module P003(
  p003) where

p003 :: Int
p003 = maximum $ factors 600851475143

primes :: [Int]
primes = 2 : sieve primes [3,5..]
  where
    sieve (p:pt) xs =
      let (lesser, higher) = span (< p * p) xs
      in lesser ++ sieve pt [ x | x <- higher, mod x p /= 0 ]

factors :: Int -> [Int]
factors n
  | null divisors = [n]
  | otherwise = v : factors (div n v)
  where
    v = head divisors
    divisors = [ i | i <- [2..pred n], mod n i == 0 ]
