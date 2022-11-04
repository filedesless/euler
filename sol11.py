from math import prod


def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix[i]))] for i in range(len(matrix))]


assert transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [
    [1, 4, 7], [2, 5, 8], [3, 6, 9]]


def row_adj(matrix):
    return [row[i:i+4] for row in matrix for i in range(len(row)-3)]


def diag_adj(matrix):
    return [d[i:i+4] for d in diags(matrix)
            for i in range(len(d)-3) if len(d) >= 4]


def diag(matrix, offset=0):
    return [matrix[i][j] for i in range(len(matrix)) for j in range(len(matrix[i])) if i + offset == j]


def diags(matrix):
    n = len(matrix)
    m = len(matrix[0])
    return [diag(matrix, offset) for offset in range(-m + 1, n)]

def fliplr(matrix):
    return [ row[::-1] for row in matrix ]


matrix = [[int(num) for num in line.split()]
          for line in open('11.txt').readlines()]

p1 = max([prod(adj) for adj in row_adj(matrix) + row_adj(transpose(matrix))])
p2 = max([prod(adj) for adj in diag_adj(matrix) + diag_adj(fliplr(matrix))])

print(max(p1, p2))
