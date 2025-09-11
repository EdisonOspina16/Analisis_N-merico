import numpy as np
import time

def jacobi_matrices(A, b, x0, tol=1e-6):

    D = np.diag(np.diag(A))
    U = D-np.triu(A)
    L = D-np.tril(A)

    Tj = np.dot(np.linalg.inv(D), L+U)
    cj = np.dot(np.linalg.inv(D),b)

    # calcular los valores y vectores propios.
    eig, eigv = np.linalg.eig(Tj)
    radio = np.max(abs(eig))
    print(f'El radio espectral es: {radio}')

    if radio < 1:
        tiempo = time.time()
        error = 1
        iter = 0
        N_max = 100
        while error > tol and iter < N_max:
            x_new = np.dot(Tj,x0) + cj
            error = max(abs(x_new - x0)) # Norma infinito
            x0 = x_new.copy()
            iter += 1
        return x_new, iter, time.time() - tiempo
    else:
        print("No converge :(")
        return None


A = np.array([[3, -1, 0],
              [-1, 4, -1],
              [0, -1, 5]], float)

b = np.array([2, 3, 5], float)

x0 = np.array([0, 0, 0])

solucion , iter, tiempo = jacobi_matrices(A, b, x0)
print(f'La solución es: {solucion}, {iter} iteraciones')
print(f'El tiempo de ejecución es: {tiempo} segundos')