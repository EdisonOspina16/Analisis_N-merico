import sympy as sp

def newton(funcion, X0, tolerancia=1e-8):
    x = sp.symbols('x')
    df = sp.diff(funcion, x)  # Derivada simbólica

    New = x - funcion / df
    error = 1
    iteracion = 0
    while error > tolerancia:
        iteracion += 1
        X1 = New.evalf(subs={x:X0})
        error = abs(X1 - X0)
        X0 = X1
    return X1, error, iteracion
