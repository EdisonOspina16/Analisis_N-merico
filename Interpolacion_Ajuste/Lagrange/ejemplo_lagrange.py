from Interpolacion_Ajuste.Lagrange.lagrange import lagrange
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

x = sp.Symbol('x')

x_data = np.array([1, 2, 5, 10, 20, 30, 40])
y_data = np.array([56.5, 78.6, 113.0, 144.5, 181.0, 205.0, 214.5])

coef = lagrange(x_data, y_data)
print(coef)

Polinomio = lagrange(x_data, y_data)
Polinomio1 = sp.lambdify(x, Polinomio)
ux = np.linspace(min(x_data), max(x_data), 100)
plt.plot(x_data, y_data, 'or', label= 'Datos observados')
plt.plot(ux, Polinomio1(ux), 'b', label= 'Polinomio interpolante')
plt.xlabel('Presion')
plt.xlabel('Temperatura')
plt.title('Temperatura de la acetona')
plt.show()