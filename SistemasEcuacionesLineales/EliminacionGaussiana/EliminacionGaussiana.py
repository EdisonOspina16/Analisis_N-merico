# Eliminación gaussiana, bajo el supuesto que la mnatriz A es una matriz DD o EDd
# esto nos garantiza que la eliminación converge a la solución unica del sistema de ecuaciones
# sin realizar intercambio de filas o de columnas.

import numpy as np

def eliminacion_gaussiana(A, b):
    """
    Eliminación gaussiana sin pivoteo para matrices DD o EDD.
    Retorna la matriz aumentada [A|b] en forma triangular superior.
    """
    A = A.astype(float)  # asegurar tipo float
    b = b.astype(float)
    n = len(b)

    # Eliminación hacia adelante
    for i in range(n - 1):
        for j in range(i + 1, n):
            factor_lambda = A[j, i] / A[i, i]
            A[j] = A[j] - factor_lambda * A[i]
            b[j] = b[j] - factor_lambda * b[i]

    # Concatenar A y b como matriz aumentada
    Ab = np.concatenate((A, b.reshape(-1, 1)), axis=1)
    return Ab


# Ejemplo de uso
A = np.array([[-3, 2, 1],
              [ 6,-8,-2],
              [ 1,-1,-2]], float)

b = np.array([2, 1, 3], float)

Ab_resultado = eliminacion_gaussiana(A, b)
print(Ab_resultado)
