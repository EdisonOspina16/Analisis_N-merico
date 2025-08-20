from Cota.cota_taylor import cota_taylor
from SeriesTaylor.serie_taylor import serie_taylor

import numpy as np
import pandas as pd
import sympy as sp
from matplotlib import pyplot as plt


# Ejemplo 3

x = sp.symbols('x')
f = 3**-x
x0 = 1
x_point = 1
n = 5

# f = funcion que debe ser simbolica.
# x0 = punto al rededor donde se construyeel polinomio
# n = Grado del polinomio

Poly = serie_taylor(f,x0,n)
print("El 5-ésimo polinomio de taylor es: ", Poly)

print(cota_taylor(f,x0,x_point, n))

def P(i):
    return Poly.evalf(subs={x:i})
F = sp.lambdify(x, f)

values = []
for i in [1,1.5]:
    values.append([i,P(i), F(i), abs(P(i)-F(i)), abs((P(i)-F(i))/F(i))])
Data = pd.DataFrame(data = values, columns=['x', 'P(x)', 'f(x)', '|P(x)-f(x)|', 'E_r'])
print(Data)

# Grafica:
ux = np.linspace(-2,2,500)

# función
f_num = sp.lambdify(x, f)
p_num = sp.lambdify(x, Poly)
plt.plot(ux, f_num(ux), 'r', label='f(x)')
plt.plot(ux, p_num(ux), 'b', label='P(x)')
plt.legend()
plt.show()
