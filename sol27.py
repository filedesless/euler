from itertools import takewhile
from primes import is_prime


def pol(a, b):
    n = 0
    while True:
        yield n ** 2 + a * n + b
        n += 1


(n, a, b) = max([(len(list(takewhile(is_prime, pol(a, b)))), a, b)
                 for a in range(-1000, 1001)
                 for b in range(-1000, 1001)])

print(n, a, b, a * b)
