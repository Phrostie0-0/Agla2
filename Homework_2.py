# Ruslan Nasibullin DSAI-05
def print_matrix(m):
    for row in m:
        for i in row:
            print(round(i, 5), end=" ")
        print()

def identity(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

def gaussian(m):
    n = len(m)
    inv = identity(n)
    for i in range(n):
        max_row = i
        for j in range(i + 1, n):
            if abs(m[j][i]) > abs(m[max_row][i]):
                max_row = j
        m[i], m[max_row] = m[max_row], m[i]
        inv[i], inv[max_row] = inv[max_row], inv[i]
        if m[i][i] == 0:
            raise ValueError("The matrix has no inverse")
        div = m[i][i]
        for j in range(n):
            m[i][j] /= div
            inv[i][j] /= div
        for j in range(n):
            if j != i:
                factor = m[j][i]
                for k in range(n):
                    m[j][k] -= factor * m[i][k]
                    inv[j][k] -= factor * inv[i][k]
    return inv

def inv_m(m):
    n = len(m)
    if len(m[0]) != n:
        raise ValueError("The matrix should be square")
    inv = gaussian(m)
    return inv

m = [
    [4, 7, 5],
    [2, 6, 1],
    [2, 8, 3]
]

try:
    inv = inv_m(m)
    print("Inverse matrix:")
    print_matrix(inv)
except ValueError as e:
    print(e)
