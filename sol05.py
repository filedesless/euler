"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
from math import prod, sqrt
from bench import bench


def is_prime(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(sqrt(n)) + 1))


assert all(map(is_prime, [2, 3, 5, 7, 11]))
assert not any(map(is_prime, [1, 4, 6, 8, 9, 10]))


def primes(n, l=[2]):
    """Primes up to n (with cheeky memoization)"""
    for i in range(l[-1] + 1, n + 1, l[-1]):
        if is_prime(i):
            l.append(i)
    return [p for p in l if p <= n]


assert primes(42) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]


def prime_fact(n):
    """Prime factorization of n as a list of prime and their respective powers"""
    d = {}
    for p in primes(n):
        while n % p == 0:
            d[p] = d.get(p, 0) + 1
            n //= p
    return d


assert prime_fact(100) == {2: 2, 5: 2}


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
