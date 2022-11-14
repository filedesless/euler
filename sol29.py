def solve(n):
    return len({a**b for a in range(2, n+1) for b in range(2, n+1)})


assert solve(5) == 15

print(solve(100))
