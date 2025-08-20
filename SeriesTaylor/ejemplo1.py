from Cota.cota_taylor import cota_taylor
from SeriesTaylor.serie_taylor import serie_taylor


import numpy as np
import pandas as pd
import sympy as sp
from matplotlib import pyplot as plt


x = sp.symbols('x')
f = sp.exp(2*x)*sp.sin(x)
x0 = 0
x_point = 1
n = 3


# Imprime la cota del error para el polinomio de Taylor en x=1
print("la cota de taylor es: ", cota_taylor(f,x0,x_point, n))
print("----------")


# Calcula el polinomio de Taylor de orden 3
Poly = serie_taylor(f,x0,n)
print("el polinomio de taylor es: ", Poly)
print("----------")

def P(i):
    """Evalúa el polinomio de Taylor en un punto"""
    return Poly.evalf(subs={x:i})

F = sp.lambdify(x, f) # Convierte f(x) en una función evaluable numéricamente

values = []
for i in [0.5, 1.5, 10]:
    values.append([i,P(i), F(i), abs(P(i)-F(i)), abs((P(i)-F(i))/F(i))])

Data = pd.DataFrame(values, columns=['x', 'P(x)', 'f(x)', '|P(x)-f(x)|', 'Error relativo'])
print(Data)
print("----------")

