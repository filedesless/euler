from sol12 import factors
from functools import cache


@cache
def divisors(n):
    return factors(n) - {n}


assert divisors(220) == {1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110}
assert divisors(284) == {1, 2, 4, 71, 142}


@cache
def d(n):
    return sum(divisors(n))


assert d(220) == 284
assert d(284) == 220


def amicable(a, b):
    return d(a) == b and d(b) == a


l = [(a, b) for a in range(10_001) for b in range(a) if amicable(a, b)]

print(l)
print(sum(a + b for (a, b) in l))
