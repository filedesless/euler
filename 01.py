from timeit import timeit


def iterative(a, b, n):
    """First solution"""
    return sum(i for i in range(n) if i % a == 0 or i % b == 0)


def s(n):
    """Constant time equivalent to sum(i for i in range(n+1))"""
    return n*(n+1)//2


def m(n, u):
    """Sum of multiples of n up to u
       sum(i for i in range(1, u + 1, n))
    == sum(n*i for i in range(1, u // n))
    == n*sum(i for i in range(1, u // n))
    """
    return n * s(u // n)


def constant(a, b, u):
    """Sum of the multiples of a or b before u
        Sum of the multiples of a
    +   Sum of the multiples of b
    -   Sum of the multiples of a and b (multiples of a*b)
    """
    return m(a, u - 1) + m(b, u - 1) - m(a*b, u - 1)


def bench(f, n):
    a, b = 3, 5
    t = timeit(lambda: f(a, b, n), number=10000)
    print(f"{f.__name__}({a}, {b}, {n}) = {f(a, b, n)} ran in {t}s")


# tests
for n in range(1, 10):
    for u in range(n, 100):
        assert sum(i for i in range(1, u+1, n)), m(n, u)

assert iterative(3, 5, 10) == constant(3, 5, 10) == 23
assert iterative(3, 5, 1000) == constant(3, 5, 1000)

# benchmarks
for i in range(1, 4):
    bench(iterative, 10**i)
    bench(constant, 10**i)
