from math import factorial
import numpy as np
import sympy as sp


x = sp.symbols('x') # Definición de la variable simbólica x

def cota_taylor(f, x0, x_point, n):
    # Genera un rango de valores entre x0 y x_point
    ux = np.linspace(min(x0, x_point), max(x0, x_point), 500)
    df = sp.diff(f,x,n+1) # calcula la derivada
    df = sp.lambdify(x, df) # Convierte la derivada simbólica en función numérica
    max_df = max(abs(df(ux)))
    R_n = max_df*abs(x_point-x0)**(n+1)/factorial(n+1)
    return R_n
