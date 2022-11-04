
def collatz(n):
    assert n >= 1
    yield n
    while n != 1:
        n = n // 2 if n & 1 == 0 else 3 * n + 1
        yield n


assert list(collatz(13)) == [13, 40, 20, 10, 5, 16, 8, 4, 2, 1]

print(max([list(collatz(i)) for i in range(1, 1_000_001)], key=len)[0])
