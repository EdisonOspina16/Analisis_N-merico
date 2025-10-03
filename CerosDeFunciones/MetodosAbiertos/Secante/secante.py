def secante(funcion, x0, x1, tolerancia=1e-8, n_max=100):
    iteracion = 0
    while iteracion < n_max:
        if funcion(x1) - funcion(x0) == 0:
            print("División por cero. El método de la secante no puede continuar.")
            return x1, iteracion   # devolvemos lo último calculado

        x2 = x1 - funcion(x1) * (x1 - x0) / (funcion(x1) - funcion(x0))
        iteracion += 1

        if abs(x2 - x1) < tolerancia or abs(funcion(x2)) < tolerancia:
            return x2, iteracion

        x0, x1 = x1, x2

    # Si no converge, devolvemos el último valor calculado en vez de None
    print("Advertencia: No se alcanzó la convergencia en el número máximo de iteraciones.")
    return x2, iteracion
