import sympy as sp

x = sp.Symbol('x')

def lagrange(x_d, y_d):
    n = len(x_d)

    P=0
    for i in range(n):
        li = 1
        for j in range(n):
            if j != i:
                li *= (x - x_d[j]) / (x_d[i] - x_d[j])
        P += li * y_d[i]
    return sp.expand(P)
