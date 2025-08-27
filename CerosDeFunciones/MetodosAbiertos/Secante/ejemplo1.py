from CerosDeFunciones.MetodosAbiertos.Secante.secante import secante


import numpy as np
import matplotlib.pyplot as plt


f = lambda x: x**10 - 1
raiz, iteraciones = secante(f, 0, 3, 1e-8, n_max=1000)
print(f"Raíz aproximada: {raiz} en {iteraciones} iteraciones")


#Gráfica
x = np.linspace(-0.5, 3.5, 1000)
y = f(x)

plt.figure(figsize=(12, 7))
plt.plot(x, y, label='$f(x) = x^{10} - 1$', color='blue', linewidth=2)
plt.axhline(0, color='yellow', linewidth=0.8)
plt.xlabel('x', fontsize=12)
plt.ylabel('f(x)', fontsize=12)
plt.title('Gráfica de $f(x) = x^{10} - 1$', fontsize=14)
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()