from itertools import permutations

if __name__ == '__main__':
    digits = [chr(ord('0') + i) for i in range(10)]
    print(sorted([''.join(p) for p in permutations(digits)])[1_000_000 - 1])
