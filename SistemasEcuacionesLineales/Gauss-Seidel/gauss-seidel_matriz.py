import numpy as np

def gauss_seidel_matrices(A, b, x0, tol=1e-6, iter=100):
    D = np.diag(np.diag(A))  # diagonal
    U = D - np.triu(A)
    L = D - np.tril(A)

    Tg = np.dot(np.linalg.inv(D - L), U)
    cg = np.dot(np.linalg.inv(D-L), b)

    # calcular los valores y vectores propios.
    eig, eigv = np.linalg.eig(Tg)
    radio = np.max(abs(eig))
    print(f'El radio espectral es: {radio}')

    if radio < 1:
        error = 1
        iter = 0
        N_max = 100
        while error > tol and iter < N_max:
            x_new = np.dot(Tg, x0) + cg
            error = max(abs(x_new - x0))  # Norma infinito
            x0 = x_new.copy()
            iter += 1
        return x_new, iter
    else:
        print("No converge :(")
        return None


# Ejemplo
A = np.array([[3, -1, 0],
              [-1, 4, -1],
              [0, -1, 5]], float)

b = np.array([2, 3, 5], float)

x0 = np.array([0,0,0])

sol, iter = gauss_seidel_matrices(A, b, x0)
print(f"Solución aproximada es: {sol}, iteraciones: {iter}")
