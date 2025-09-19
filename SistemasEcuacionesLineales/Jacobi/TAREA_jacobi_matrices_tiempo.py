import matplotlib.pyplot as plt
import numpy as np
import time

def jacobi_matrices(A, b, x0, tol=1e-6):
    D = np.diag(np.diag(A))
    U = D - np.triu(A)
    L = D - np.tril(A)

    Tj = np.dot(np.linalg.inv(D), L + U)
    cj = np.dot(np.linalg.inv(D), b)

    # Calcular los valores propios (para radio espectral)
    eig, eigv = np.linalg.eig(Tj)
    radio = np.max(abs(eig))
    print(f'El radio espectral es: {radio}')

    errores = []  # lista para guardar errores

    if radio < 1:
        tiempo = time.time()
        error = 1
        iter = 0
        N_max = 100
        while error > tol and iter < N_max:
            x_new = np.dot(Tj, x0) + cj
            error = max(abs(x_new - x0))  # Norma infinito
            errores.append(error)         # Guardamos el error
            x0 = x_new.copy()
            iter += 1
        return x_new, iter, time.time() - tiempo, errores
    else:
        print("No converge :(")
        return None, 0, 0, []

# --- Ejemplo ---
A = np.array([[3, -1, 0],
              [-1, 4, -1],
              [0, -1, 5]], float)

b = np.array([2, 3, 5], float)
x0 = np.array([0, 0, 0])

solucion, iteraciones, tiempo, errores = jacobi_matrices(A, b, x0)

print(f'La solución es: {solucion}, en {iteraciones} iteraciones')
print(f'Tiempo de ejecución: {tiempo} segundos')

# --- Gráfica del error ---
plt.figure(figsize=(8,5))
plt.semilogy(range(1, len(errores)+1), errores, 'o--', label='Jacobi Matrices')
plt.xlabel('Iteraciones')
plt.ylabel('Error (Norma infinito)')
plt.title('Convergencia del método de Jacobi')
plt.legend()
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.show()
