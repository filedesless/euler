from sol12 import factors
from functools import cache


@cache
def proper_divisors(n):
    return factors(n) - {n}


@cache
def alliquot(n):
    return sum(proper_divisors(n))


def amicable(a, b):
    return alliquot(a) == b and alliquot(b) == a


if __name__ == '__main__':
    assert proper_divisors(220) == {1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110}
    assert proper_divisors(284) == {1, 2, 4, 71, 142}

    assert alliquot(220) == 284
    assert alliquot(284) == 220

    l = [(a, b) for a in range(10_001) for b in range(a) if amicable(a, b)]

    print(l)
    print(sum(a + b for (a, b) in l))
