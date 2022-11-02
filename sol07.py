from primes import primes


def take(n, iter):
    return [x for _, x in zip(range(n), iter)]


print(take(10_001, primes())[-1])
