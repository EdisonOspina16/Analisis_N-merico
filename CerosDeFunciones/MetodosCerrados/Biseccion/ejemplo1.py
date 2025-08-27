from CerosDeFunciones.MetodosCerrados.Biseccion.biseccion import biseccion

import numpy as np

y = 1
y0 = 2
vo = 20
x = 35
g = 9.8
tolerancia = 1e-8


f_trayectoria = lambda w: x*np.tan(w)-(g*x**2)/(2*vo**2*(np.cos(w))**2)+y0-y
theta, iteracion = (biseccion(f_trayectoria, 0, np.pi/4, tolerancia))
print("el angulo inicial es: ", np.degrees(theta))