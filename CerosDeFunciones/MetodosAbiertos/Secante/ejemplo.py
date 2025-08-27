from CerosDeFunciones.MetodosAbiertos.Secante.secante import secante


import numpy as np
import matplotlib.pyplot as plt


# Definir la función
f = lambda x: np.sin(x) - np.exp(-x)

# Graficar la función en el intervalo [0,10]
array = np.linspace(0, 10, 100)
plt.axhline(0, color="black", linewidth=0.8, linestyle="--")  # Eje X
plt.plot(array, f(array), 'r', label="f(x) = sin(x) - exp(-x)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Gráfico de la función f(x)")
plt.legend()
plt.grid(True)
plt.show()


# Probar con la función
raiz, iteraciones = secante(f, 0, 2, 1e-6)
print(f"Raíz aproximada: {raiz}, Iteraciones: {iteraciones}")
