import numpy as np

def eliminacion_gaussiana_pivote(A, b):
    """
    Eliminación gaussiana con pivoteo parcial.
    Retorna la matriz triangular superior A y la solución x en formato [A|x].
    """
    A = A.astype(float)
    b = b.astype(float)
    n = len(b)

    # Matriz aumentada inicial [A|b]
    Ab = np.concatenate((A, b.reshape(-1, 1)), axis=1)
    print("Matriz aumentada inicial [A|b]:\n", Ab, "\n")

    # Eliminación hacia adelante con pivoteo parcial
    for i in range(n - 1):
        if A[i, i] == 0:
            A[[i, i+1]] = A[[i+1, i]]
            b[[i, i+1]] = b[[i+1, i]]

        for j in range(i + 1, n):
            factor_lambda = A[j, i] / A[i, i]
            A[j] = A[j] - factor_lambda * A[i]
            b[j] = b[j] - factor_lambda * b[i]

    # Sustitución regresiva
    x_solucion = np.zeros_like(b)
    for k in range(n - 1, -1, -1):
        x_solucion[k] = (b[k] - np.dot(A[k, k+1:n], x_solucion[k+1:n])) / A[k, k]

    # Mostrar matriz triangular superior con columna de solución [A|x]
    Ax_final = np.concatenate((A, x_solucion.reshape(-1, 1)), axis=1)
    print("Matriz triangular superior con solución [A|x]:\n", Ax_final, "\n")

    return Ax_final, x_solucion


# Ejemplo de uso
A = np.array([[0, 2, 1],
              [6, -8, -2],
              [1, -1, -2]], float)

b = np.array([2, 1, 3], float)

Ax_resultado, solucion = eliminacion_gaussiana_pivote(A, b)
