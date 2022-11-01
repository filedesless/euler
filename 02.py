def fib(u):
    """Fibonacci generator for values up to u"""
    a = 1
    b = 2
    while a <= u:
        yield a
        c = a
        a = b
        b = b + c


assert list(fib(100)) == [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

print(sum(i for i in fib(4_000_000) if i & 1 == 0))
