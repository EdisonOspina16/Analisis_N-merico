from CerosDeFunciones.MetodosCerrados.Biseccion.biseccion import biseccion

import numpy as np

l = 10
r = 1
V = 10
funcion = lambda h: l * (0.5 * np.pi * r ** 2 - r ** 2 * np.arcsin(h / r) - h * (r ** 2 - h ** 2) ** (1 / 2)) - V

h,i = biseccion(funcion, 0,r,1e-8)
print("la profundidad del abrevadero es: ", 1 - h)
