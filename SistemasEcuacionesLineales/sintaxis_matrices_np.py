import numpy as np

A = np.array([[-3, 2, 1],[6, -8, -2],[1, -1, -2]], float)
print(A)
print("inversa de una matriz")


A_inversa = np.linalg.inv(A)
print(A_inversa)

print("Elementos de la diagonal de una matriz")
DIAGONAL = np.diag(A)
print(DIAGONAL)

matriz_diagonal = np.diag(DIAGONAL)
print(matriz_diagonal)

# Matriz triangular superior
print(" Matriz Triangular Superior")
U = np.triu(A)
print(U)

# Matriz transpuesta
print("Matriz transpuesta")
AT = np.transpose(A)
print(AT)

# producto punto
print(np.dot(AT, DIAGONAL))

# determinante
np.linalg.det(A)