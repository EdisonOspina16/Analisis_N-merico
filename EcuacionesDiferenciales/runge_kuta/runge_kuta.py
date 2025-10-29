import numpy as np


def runge4(funcion, a, b, h, co):
    n = int((b - a) / h)
    t = np.linspace(a, b, n+1)
    wr = [co] # condición inicial o las condiciones iniciales
    for i in range(n):
        k1 = h * funcion(t[i], wr[i])
        k2 = h * funcion(t[i] + 0.5 * h , wr[i]+ 0.5 * k1)
        k3 = h * funcion(t[i] + 0.5 * h , wr[i]+ 0.5 * k2)
        k4 = h * funcion(t[i+1], wr[i]+ 0.5 * k3)
        wr.append(wr[i] + (1/6) * (k1 + 2 * k2 + 2 * k3 + k4))
    return t, wr


# funcion = lambda t, y: t*np.exp(3*t)-2*y
# t, y = runge4(funcion, 0, 1, 0.25, 0)
# print(t, y)
