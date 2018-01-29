let solution =
  let max = 600851475143 in

  let largest_prime_factor (n: int): int =
    let rec aux d i =
      if i = d then i else
      if i mod d = 0
      then aux d (i / d)
      else aux (succ d) i
    in aux 2 n in

  largest_prime_factor max
;;
