from CerosDeFunciones.MetodosAbiertos.Newton.newton import newton
import sympy as sp

x=sp.symbols('x')

funcion = x**2-6
print(newton(funcion,10,1e-8))

