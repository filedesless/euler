from math import gcd

for n in range(1, 100):
    for m in range(n + 1, 100):
        if gcd(m, n) == 1 and not (n & 1 == 0 and m & 1 == 0):
            for k in range(1, 100):
                a, b, c = k*(m*m - n*n), k*2*m*n, k*(m*m + n*n)
                if a + b + c == 1000:
                    print(a * b * c)
