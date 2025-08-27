from CerosDeFunciones.MetodosCerrados.Biseccion.biseccion import biseccion
from CerosDeFunciones.MetodosAbiertos.Newton.newton import newton
from CerosDeFunciones.MetodosCerrados.PosicionFalsa.posicion_falsa import posicion_falsa


import sympy as sp
import numpy as np

# Variables y parámetros
x = sp.symbols('x')
r = 1
V = 0.75

funcion = (sp.pi * x**2 * (3*r - x)) / 3 - V
h, error, iteracion = newton(funcion, 0.5, 1e-6)
print(f'La profundidad del agua con Newton es: {h:.6f} m')
print(f'Iteraciones: {iteracion}')



funcion_para_biseccion_y_posicion_falsa = lambda h: (np.pi*h**2*(3*r - h)/3)- V

h2, iteacion2 = biseccion(funcion_para_biseccion_y_posicion_falsa, 0,2, 1e-6,)
print('La profundida del agua del abrevadero con el metodo de biseccion es:', h2)

h3,iteraciones3 = posicion_falsa(funcion_para_biseccion_y_posicion_falsa,0,2,1e-6)
print('La profundida del agua del abrevadero con el metodo de posición falsa es:', h3)