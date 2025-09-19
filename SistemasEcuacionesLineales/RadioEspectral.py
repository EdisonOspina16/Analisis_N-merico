import numpy as np

A = np.array([[2, 1, 0],
              [0, 3, 1],
              [0, 0, 4]], float)

B = np.array([[-1, 2, 0],
              [2, -3, 1],
              [0, 1, 2]], float)


# eingenvalues, eingen_vect =np.linalg.eig(MATRIZ)
valores_propios , vectores_propios  = np.linalg.eig(A)
print(f" Los valores propios de la matriz B son. {valores_propios}")

# radio
radio = max(abs(valores_propios))
print(f" El radio espectral de la matriz A es {radio}")