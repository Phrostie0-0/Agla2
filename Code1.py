# Ruslan Nasibullin DSAI-05
import sympy as sp

N = int(input("Enter the number of variables: "))
print(f"Enter the elements of the matrix {N}x{N+1} by line separated by a space:")
m1 = []
for i in range(N):
    row = list(map(float, input(f"Line {i + 1}: ").split()))
    m1.append(row)
m2 = sp.Matrix(m1)
rref, pivots = m2.rref()
print(f"Solution for system with {N} variables:")
for i in pivots:
    print(round(rref[i, N], 3), end=" ")
