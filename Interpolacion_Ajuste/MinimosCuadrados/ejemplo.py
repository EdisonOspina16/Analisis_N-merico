from Interpolacion_Ajuste.MinimosCuadrados.minimos_cuadrados import minimos_cuadrados
import matplotlib.pyplot as plt
import numpy as np

x_data = np.array([0, 2, 3, 6, 7])
y_data = np.array([0.120, 0.153, 0.170, 0.225, 0.260])

m,b = minimos_cuadrados(x_data, y_data)
print(f" La pendiente es: {m}, y el intervalo es {b}")


# Grafica
ux = np.linspace(min(x_data), max(x_data), 2)
P = lambda x: m* x+b
plt.plot(x_data, y_data, 'or', label='datos observados')
plt.plot(ux,P(ux), 'b', label='regresión')
plt.xlabel('Fuerza(kgf)')
plt.ylabel('Elongación(m)')
plt.title('fuerza aplicada a un resorte')
plt.legend()
plt.show()