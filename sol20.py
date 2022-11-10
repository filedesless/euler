from math import prod


def fact(n): return prod(range(1, n+1))


assert fact(10) == 3628800


def solve(n):
    return sum([int(c) for c in str(fact(n))])


assert solve(10) == 27

print(solve(100))
