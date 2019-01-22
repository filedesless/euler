module Main where

import P001
import P002

format :: Show a => (Integer, a) -> String
format (i, v) = "Problem " ++ show i ++ ": " ++ show v

solved = [p001, p002]

main :: IO ()
main = do
  mapM_ (putStrLn . format) $ zip [1..] solved
