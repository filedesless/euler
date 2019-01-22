module Main where

import P001
import P002
import P003
import P004

format :: Show a => (Integer, a) -> String
format (i, v) = "Problem " ++ show i ++ ": " ++ show v

solved = [p001, p002, p003, p004]

main :: IO ()
main = do
  mapM_ (putStrLn . format) $ zip [1..] solved
