def factors(n):
    return {x for i in range(1, int(n**0.5)+1)
            for x in [i, n//i] if n % i == 0}


def isPrime(n):
    return n >= 2 and factors(n) == {1, n}


def primeFactors(n):
    return {f for f in factors(n) if isPrime(f)}


assert primeFactors(13195) == {5, 7, 13, 29}

if __name__ == '__main__':
    print(max(primeFactors(600851475143)))
