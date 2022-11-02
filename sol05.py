"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
from math import prod
from bench import bench
from primes import prime_fact


def gcd(a, b):
    """Euclidean GCD"""
    if b == 0:
        return a
    if a < b:
        return gcd(b, a)
    return gcd(b, a % b)


assert gcd(18, 48) == 6


def lcm(a, b):
    """Least common multiple"""
    return a * b // gcd(a, b)


assert lcm(21, 6) == 42


def solve_a(n):
    d = {}
    for i in range(2, n + 1):
        for (prime, power) in prime_fact(i).items():
            d[prime] = max(d.get(prime, 0), power)
    return prod(p**c for (p, c) in d.items())


assert solve_a(10) == 2520


def solve_b(n):
    acc = 1
    for i in range(2, n):
        acc = lcm(acc, i)
    return acc


assert solve_b(10) == solve_a(10)

if __name__ == '__main__':
    for i in range(1, 3):
        bench(solve_a, 10, 10**i)
        bench(solve_b, 10, 10**i)
