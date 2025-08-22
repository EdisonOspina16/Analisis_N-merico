from CerosDeFunciones.MetodosCerrados.Biseccion.biseccion import biseccion

import numpy as np
import matplotlib.pyplot as plt


array_x = np.linspace(0,20,1000)
f_dos_numeros = lambda x: (x+ np.sqrt(x))*(20-x+np.sqrt(20-x))-155.55


plt.plot(array_x, f_dos_numeros(array_x))
plt.axhline(0, linestyle='--', color='red')
plt.grid()
plt.show()

x, iteraciones = biseccion(f_dos_numeros, 5,7.5, 1e-8)
y, iteraciones2 = biseccion(f_dos_numeros, 12.5,15, 1e-8)
print(f"Las soluciones son: {x}, {y} y la suma es {x + y}")