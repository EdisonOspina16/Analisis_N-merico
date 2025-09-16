def biseccion(funcion,a, b, tolerancia):

    if funcion(a) * funcion(b) > 0:
        print("El método de bisección no garantiza la convergencia en este intervalo.")
        return None

    iteracion = 0
    while abs(b - a) > tolerancia:
        c = (a + b) / 2
        iteracion += 1
        if abs(funcion(c)) < tolerancia:
            return c, iteracion
        if funcion(a) * funcion(c) < 0:
            b = c
        else:
            a = c
    return c, iteracion
