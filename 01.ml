let solution: int =
  let max: int = 1000
  and add (x: int): int =
    if x mod 3 = 0 || x mod 5 = 0
    then x
    else 0
  in
  let rec findMul (i: int) (sum: int): int =
    if i >= max
    then sum
    else findMul (i + 1) (sum + add i)
  in findMul 0 0
;;
