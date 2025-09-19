import numpy as np


def matriz_polinomial(x_data):

    n = len(x_data)

    # declarar una matriz de ceros para llenar dependiente de los valores de x_data
    M = np.zeros([n,n], float)
    M[0:n,0] = 1
    for i in range(n):
        for j in range(1, n):
            M[i,j] = M[i, j-1]*x_data[i]
    return M

