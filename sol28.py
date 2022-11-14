dx = 2
x = 1
s = 1
for n in range(1, 501):
    x += dx
    dx += 8
    s += 4*x + 6*2*n
print(f"{2*n+1}x{2*n+1} => {s}")
