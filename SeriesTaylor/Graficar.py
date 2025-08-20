import matplotlib.pyplot as plt
import numpy as np

# Graficamos el polinomio de grado 2:
ux = np.linspace(-2, 5, 500)

# Función
#f = lambda x: np.log(x**2 + 1)
def f(x):
    return np.log(x**2+1)

# polinomio
P = lambda x: x**2

plt.plot(ux, f(ux), 'r')
plt.plot(ux, P(ux), 'b')
plt.legend()
plt.show()
print("-----------------------")

