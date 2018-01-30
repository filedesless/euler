#!/usr/bin/env python3

def largest_prime_factor(n:int) -> int:
    i = n
    d = 2

    while i != d:
        if i % d == 0: i //= d
        else: d += 1

    return i

print(largest_prime_factor(600851475143))
