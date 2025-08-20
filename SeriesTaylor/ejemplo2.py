from Cota.cota_taylor import cota_taylor
from SeriesTaylor.serie_taylor import serie_taylor

import numpy as np
import pandas as pd
import sympy as sp
from matplotlib import pyplot as plt

x = sp.symbols('x')
funcion = sp.exp(2*x)*sp.cos(2*x)
x0 = 0
x_point = 0.5 # cota de truncamiento
n = 6 # grado del polinomio

Poly = serie_taylor(funcion,x0,n)
print("La serie de taylor es: ", Poly)
print("------")


#  Use el polinomio para aproximar P(1), P(4.5)
#  y calcule el error relativo y el error absoluto

def P(i):
    return Poly.evalf(subs={x:i})

F = sp.lambdify(x, funcion) # Convierte f(x) en una función evaluable numéricamente

values = []
for i in [1,4.5]:
    values.append([i,P(i), F(i), abs(P(i)-F(i)), abs((P(i)-F(i))/F(i))])

# Se crea un dataframe con los resultados
Data = pd.DataFrame(data = values, columns=['x', 'P(x)', 'f(x)', '|P(x)-f(x)|', 'E_r'])
print(Data)
print("------")

cota = cota_taylor(funcion,x0,x_point,n)
print("La cota de truncamiento de Taylor es: ", cota)
print("------")


# Graficamos
ux =  np.linspace(-2, 2, 500)

# Convierte el polinomio de Taylor en función numérica
f_num = sp.lambdify(x, funcion)
p_num = sp.lambdify(x, Poly)

# Grafica la función original y el polinomio de Taylor
plt.plot(ux, f_num(ux), 'r', label='f(x)') # f(x) en rojo
plt.plot(ux, p_num(ux), 'b', label='P(x)') # P(x) en azul
plt.legend()
plt.show()
