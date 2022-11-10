from collections import deque
from typing import List, Tuple

lines = [[int(word) for word in line.strip().split()]
         for line in open('18.txt').readlines()]


def check(lines: List[List[int]], row: int, col: int) -> Tuple[deque, int]:
    current = lines[row][col]
    if row >= len(lines) - 1:
        return (deque([current]), current)
    (pa, gleft) = check(lines, row + 1, col)
    (pb, gright) = check(lines, row + 1, col + 1)
    if gleft < gright:
        pb.appendleft(current)
        return (pb, current + gright)
    else:
        pa.appendleft(current)
        return (pa, current + gleft)


(p, x) = check(lines, 0, 0)
print(p, sum(p), x)
assert sum(p) == x
assert len(p) == len(lines)
assert p[0] == lines[0][0]
assert p[-1] in lines[-1]
