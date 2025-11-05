import numpy as np

def euler(funcion, a, b, h, condicion_inicial):
    """
    :parametro función: función f(t, z) que devuelve un array con derivadas
    :parametro a: límite inferior
    :parametro b: límite superior
    :parametro h: paso

    #Prueba rápida / exploración -> h = 0.1 o 0.5 -> Menos preciso, pero rápido
    #Quieres buena precisión	-> h = 0.01 o 0.001 ->	Más puntos, más lento
    #Ecuaciones suaves y simples -> h = 0.2 o 0.25	-> Suficiente en muchos casos

    :parametro condición_inicial: vector de condiciones iniciales [x0, y0]
    :retorna: arrays t y w (solución)
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

#a = 0
#b = 1
#h = 0.5
#co = np.array([0, 0])
#print(euler(funcion, a, b, h, co))