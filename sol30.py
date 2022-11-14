
def pred(n, p):
    return sum([int(c)**p for c in str(n)]) == n


assert sum([n for n in range(2, 10_000) if pred(n, 4)]) == 19316

# 7 * 9**5 < 1_000_000
# => a number above 1_000_000 can't be the sum of it's digits 5th powers
print(sum([n for n in range(2, 1_000_000) if pred(n, 5)]))
