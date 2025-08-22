def posicion_falsa(funcion, a, b, tolerancia):

    if funcion(a) * funcion(b) >= 0:
        print("El intervalo no contiene una raíz.")
        return None

    iteracion = 0
    c = b - funcion(b) * (a - b) / (funcion(a) - funcion(b))
    while abs(c) > tolerancia:
        c = b - funcion(b) * (a - b) / (funcion(a)-funcion(b))
        iteracion += 1
        if abs(funcion(c))<tolerancia:
            return c, iteracion
        if funcion(a) * funcion(c )< 0:
            b = c
        else:
            a = c
    return c, iteracion
