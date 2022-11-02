from math import prod
from bench import bench

s = "".join([line.strip() for line in open('08.txt').readlines()])
n = len(s)


def maxprod(size):
    slices = [s[i:i+size] for i in range(n-size+1)]
    return max(prod(int(d) for d in digits) for digits in slices)


assert maxprod(4) == 5832

print(maxprod(13))
