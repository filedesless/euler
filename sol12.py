def triangle_numbers():
    n = 1
    while True:
        yield n*(n+1)//2
        n += 1


def take(n, i):
    return [x for (_, x) in zip(range(n), i)]


assert take(10, triangle_numbers()) == [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]


def factors(n):
    return {x for i in range(1, int(n**0.5) + 1) if n % i == 0 for x in (i, n // i)}


t = {
    1: {1},
    3: {1, 3},
    6: {1, 2, 3, 6},
    10: {1, 2, 5, 10},
    15: {1, 3, 5, 15},
    21: {1, 3, 7, 21},
    28: {1, 2, 4, 7, 14, 28},
}
for (n, l) in t.items():
    assert factors(n) == l


def solve(n):
    for t in triangle_numbers():
        f = factors(t)
        if len(f) > n:
            return t


assert solve(5) == 28

print(solve(500))
