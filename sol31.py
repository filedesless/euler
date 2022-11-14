from bench import bench
from functools import cache

l = [1, 2, 5, 10, 20, 50, 100, 200]


@cache
def solve(n: int, s: int) -> int:
    if s == 0:
        return 1
    if s < 0:
        return 0
    if n < 0:
        return 0
    return solve(n - 1, s) + solve(n, s - l[n])


bench(solve, 1000, len(l) - 1, 200)
