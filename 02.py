#!/usr/bin/env python3

memo = dict()
def fib(n: int) -> int:
    if n in memo: return memo[n]
    elif n <= 2: return n
    else: 
        val = fib(n-1) + fib(n-2)
        memo[n] = val
        return val

def genNumbers():
    i = 2
    while fib(i) < 4000000:
        if fib(i) % 2 == 0:
            yield fib(i)
        i += 1

print(sum(genNumbers()))
