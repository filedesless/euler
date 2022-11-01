from bench import bench


def pal(n):
    return str(n) == str(n)[::-1]


assert pal(9009)


def quad(l, n):
    """Find highest palyndromic product of numbers between l and n"""
    g = ((i, j, i * j) for i in range(l, n)
         for j in range(i + 1, n) if pal(i*j))
    return max(g, key=lambda tup: tup[2])


assert quad(10, 100) == (91, 99, 9009)


def faster(l, n):
    """Find highest palyndromic product of numbers between l and n"""
    # find highest palyndromic square n*n
    lower = next(i for i in reversed(range(l, n)) if pal(i*i))
    return quad(lower, n)


assert faster(10, 100) == (91, 99, 9009)
assert faster(100, 1000) == quad(100, 1000)

bench(quad, 10, 100, 1000)
bench(faster, 10, 100, 1000)
