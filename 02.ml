let solution: int =
  let max: int = 4000000
  and cache = Hashtbl.create 100
  in let rec fib (n: int): int =
       if Hashtbl.mem cache n
       then Hashtbl.find cache n
       else
       if n <= 2 then n
       else let v = fib (n - 2) + fib (n - 1) in
         Hashtbl.add cache n v; v
  in let value (n: int): int =
       let v = fib n in
       if v mod 2 = 0
       then v
       else 0

  in let rec add i sum =
       if fib i >= max
       then sum
       else add (succ i) (sum + value i)
  in add 0 0
;;
