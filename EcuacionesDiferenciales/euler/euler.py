import numpy as np

def euler(funcion, a, b, h, condicion_inicial):
    """
    Método de Euler para sistemas de EDOs.
    :param funcion: función f(t, z) que devuelve un array con derivadas
    :param a: límite inferior
    :param b: límite superior
    :param h: paso
    :param condicion_inicial: vector de condiciones iniciales [x0, y0]
    :return: arrays t y w (solución)
    """

    n = int((b - a) / h)
    w = [condicion_inicial]
    t = np.linspace(a, b, n+1)
    for i in range(n):
        w.append(w[i] + h * funcion(t[i], w[i]))
    return t, w


def funcion(t, z):
    """
    ¿Quién es z?: eso depende: z =[u, w]
    """
    u = z[0]
    w = z[1]
    f_1 = w
    f_2 = t * np.exp(t) - t + 2 * w - u
    return np.array([f_1, f_2])

a = 0
b = 1
h = 0.5
co = np.array([0, 0])
print(euler(funcion, a, b, h, co))