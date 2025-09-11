import numpy as np


def jacobi_suma(A, b, tolerancia, max_iter=100):
    x0 = np.zeros_like(b, dtype=float)  # Aproximación inicial
    x_new = np.zeros_like(b, dtype=float)
    error = 1
    iteraciones = 0

    while error > tolerancia and iteraciones < max_iter:
        n = len(b)
        for i in range(n):
            aux_suma = 0
            for j in range(n):
                if i != j:
                    aux_suma += np.dot(A[i, j], x0[j])
            x_new[i] = (b[i] - aux_suma) / A[i, i]

        # Calculamos error como norma infinita
        error = max(abs(x_new - x0))
        print(f"Iter {iteraciones + 1}: {x_new}, error = {error}")

        # Actualizar x0
        x0 = x_new.copy()
        iteraciones += 1

    return x_new


# Ejemplo
A = np.array([[3, -1, 0],
              [-1, 4, -1],
              [0, -1, 5]], float)

b = np.array([2, 3, 5], float)


solucion = jacobi_suma(A, b, 1e-2)
print("\nSolución aproximada:", solucion)
