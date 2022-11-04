from math import comb


def solve(n):
    return comb(2*n, n)


assert solve(2) == 6


print(solve(20))
