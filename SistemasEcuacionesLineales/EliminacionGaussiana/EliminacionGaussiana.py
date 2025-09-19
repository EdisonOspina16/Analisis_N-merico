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

    x_solucion = np.zeros_like(b)

    for k in range(n - 1, -1, -1):
        x_solucion[k] = (b[k] - np.dot(A[k, k + 1:n], x_solucion[k + 1:n])) / A[k, k]

    return x_solucion
