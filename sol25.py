u = 10 ** 999
i = 2
a = 1
b = 2
while a < u:
    c = a
    a = b
    b = b + c
    i += 1
    if i == 12:
        assert a == 144

print(i, a)
