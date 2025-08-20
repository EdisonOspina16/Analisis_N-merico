from math import factorial
import sympy as sp

# Declarar la variable simbólica
x = sp.symbols('x')

def serie_taylor(f, x0, n):
    P = 0
    for k in range(n+1):
        df = sp.diff(f, x, k) # derivada k-ésima respecto a x
        df = df.subs(x, x0).evalf() # evaluar en x0 (forma robusta)
        P += df * (x - x0)**k / factorial(k)
    return P