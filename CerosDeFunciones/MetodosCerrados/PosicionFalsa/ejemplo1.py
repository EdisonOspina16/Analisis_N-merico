from CerosDeFunciones.MetodosCerrados.PosicionFalsa.posicion_falsa import posicion_falsa


funcion=lambda x:x**2-6
print(posicion_falsa(funcion,2,3,1e-8))