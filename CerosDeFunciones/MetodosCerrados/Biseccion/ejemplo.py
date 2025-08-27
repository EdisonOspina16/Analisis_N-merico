from CerosDeFunciones.MetodosCerrados.Biseccion.biseccion import biseccion

funcion = lambda x:3**(-x)-x

resultado = biseccion(funcion, 0, 1, 1e-8)
print(resultado)