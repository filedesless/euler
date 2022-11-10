

names = sorted([line[1:-1] for line in open('22.txt').read().split(",")])


def worth(name: str) -> int:
    return sum(ord(c) - ord('A') + 1 for c in name)


print(sum([(i+1) * w for (i, w) in enumerate(map(worth, names))]))
