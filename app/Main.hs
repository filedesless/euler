module Main where

import P001
import P002
import P003
import P004
import P005
import P006
import P007

format :: Show a => (Integer, a) -> String
format (i, v) = "Problem " ++ show i ++ ": " ++ show v

solved = [p001, p002, p003, p004, p005, p006, p007]

main :: IO ()
main = do
  mapM_ (putStrLn . format) $ zip [1..] solved
