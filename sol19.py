

# first sunday of the month landed on
l = [0, 4, 4, 1, 6, 3, 1, 5, 2, 0, 4, 2]  # year 1900
s = 0

for y in range(1901, 2001):
    l = [(d-1) % 7 for d in l]
    if y % 4 == 0:
        l = l[:2] + [(d-1) % 7 for d in l[2:]]
    if y % 4 == 1 and y != 1901:  # 1900 wasn't a leap year
        l = [(d-1) % 7 for d in l[:2]] + l[2:]
    n = len([d for d in l if d == 1])
    s += n
    # print(y, l, n, s)

print(s)
