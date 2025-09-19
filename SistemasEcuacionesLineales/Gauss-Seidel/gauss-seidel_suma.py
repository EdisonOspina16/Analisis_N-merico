import numpy as np

def seidel_sumas(A,b, x0, tol=1e-6, max_iter=100):
    x_new = np.zeros_like(b)
    error = 1
    iteraciones = 0
    while error > tol and iteraciones < max_iter:
        n = len(b)
        for i in range(n):
            suma1 = 0
            suma2 = 0
            for j in range(0, i):
                suma1 = np.dot(A[i][j], x_new[j])
            for j in range(i + 1, n):
                suma2 = np.dot(A[i][j], x0[j])
            x_new[i] = (b[i]- suma1-suma2) / A[i][i]

        error = max(abs(x_new - x0))
        print(f"iter {iteraciones + 1 }: {x_new}, error = {error}")

        x0 = x_new.copy()
        iteraciones += 1
    return x_new, iteraciones

# Ejemplo
A = np.array([[3, -1, 0],
              [-1, 4, -1],
              [0, -1, 5]], float)

b = np.array([2, 3, 5], float)

x0 = np.array([0,0,0])

sol, iter  = seidel_sumas(A, b, x0)
print(f"Solución aproximada es: {sol}")


