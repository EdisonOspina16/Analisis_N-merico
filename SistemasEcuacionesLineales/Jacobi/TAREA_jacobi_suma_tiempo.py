import matplotlib.pyplot as plt
import numpy as np
import time

def jacobi_suma(A, b, tolerancia=1e-6, max_iter=100):
    x0 = np.zeros_like(b, dtype=float)  # Aproximación inicial
    x_new = np.zeros_like(b, dtype=float)
    error = 1
    iteraciones = 0
    errores = []  # lista para guardar los errores

    tiempo = time.time()
    while error > tolerancia and iteraciones < max_iter:
        n = len(b)
        for i in range(n):
            aux_suma = 0
            for j in range(n):
                if i != j:
                    aux_suma += np.dot(A[i, j], x0[j])
            x_new[i] = (b[i] - aux_suma) / A[i, i]

        # Calculamos error como norma infinito
        error = max(abs(x_new - x0))
        errores.append(error)   # guardamos error en la lista
        print(f"Iter {iteraciones + 1}: {x_new}, error = {error}")

        # Actualizar x0
        x0 = x_new.copy()
        iteraciones += 1

    return x_new, time.time() - tiempo, errores


# Ejemplo
A = np.array([[3, -1, 0],
              [-1, 4, -1],
              [0, -1, 5]], float)

b = np.array([2, 3, 5], float)

solucion, tiempo, errores = jacobi_suma(A, b)
print(f"\nSolución aproximada: {solucion}")
print(f"Tiempo de ejecución: {tiempo} segundos")

# Gráfica de error
plt.figure(figsize=(8,5))
plt.semilogy(range(1, len(errores)+1), errores, 'o--', label='Jacobi Suma')
plt.xlabel('Iteraciones')
plt.ylabel('Error (Norma infinito)')
plt.title('Convergencia del método de Jacobi (versión suma)')
plt.legend()
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.show()
