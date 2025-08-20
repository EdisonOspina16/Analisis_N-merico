from Cota.cota_taylor import cota_taylor
from SeriesTaylor.serie_taylor import serie_taylor

import numpy as np
import pandas as pd
import sympy as sp
from matplotlib import pyplot as plt


x = sp.symbols('x')                   # Variable simbólica
f = sp.exp(x) / x                     # Función
x0 = 1                                # Punto de expansión
n = 8                                 # Grado del polinomio de Taylor

# ========================================
# 1. Polinomio de Taylor de grado n
# ========================================
P_8 = serie_taylor(f, 1,8)
print("El polinomio de taylor es: ", P_8)
print("----------")

# ========================================
# 2. Evaluación de la función y del polinomio
# ========================================
def P(i):
    return P_8.evalf(subs={x: i})

F = sp.lambdify(x, f) # Definir la función original como función numéric
values = []
for i in [0.1, 0.5, 1.5, 10]:
    values.append([i, P(i), F(i), abs(P(i)-F(i)), abs((P(i)-F(i))/F(i))])

# Crear DataFrame
Data = pd.DataFrame(values, columns=['x', 'P(x)', 'f(x)', '|P(x)-f(x)|', 'E_R'])
print(Data)

x_point = 0.1
# ========================================
# 3. Cota del error en x=0.1
# ========================================
cota = cota_taylor(f, 1,0.1, 8)
print("la cota es: ", cota)
print("----------")

# ========================================
# 4. Aproximación de la integral ∫ f(x) dx en [0.5,1]
# ========================================
integral_real = sp.integrate(f, (x, 0.5, 1))
integral_aprox = sp.integrate(P_8, (x, 0.5, 1))
print("Integral exacta:", integral_real.evalf())
print("Integral aproximada con P8:", integral_aprox.evalf())
print("----------")

# ========================================
# 5. Aproximación de f'(0.5)
# ========================================
f_der = sp.diff(f, x)        # Derivada exacta
P_der = sp.diff(P_8, x)      # Derivada del polinomio
print("f'(0.5) exacto:", f_der.evalf(subs={x:0.5}))
print("f'(0.5) aproximado con P8:", P_der.evalf(subs={x:0.5}))
print("----------")

# ========================================
# 7. Gráfica de f(x) y aproximaciones
# ========================================

