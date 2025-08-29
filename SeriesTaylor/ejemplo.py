from SeriesTaylor.serie_taylor import serie_taylor

import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
import pandas as pd


# Declarar la variable simbólica
x = sp.symbols('x')

# Definir función simbólica
f = sp.log(x**2 + 1)
x0 = 0
n = 2

# Calcular el polinomio de Taylor
Poly = serie_taylor(f, x0, n)
print("Polinomio de Taylor:", Poly)
print("---------------")

def P(i):
    return Poly.evalf(subs={x: i})

# Definir la función original como función numérica
F = sp.lambdify(x, f)

# Calcular valores para x = 1 y x = 5
values = []
for i in [1, 5]:
    values.append([i, P(i), F(i), abs(P(i)-F(i)), abs((P(i)-F(i))/F(i))])

# Crear DataFrame
Data = pd.DataFrame(values, columns=['x', 'P(x)', 'f(x)', '|P(x)-f(x)|', 'E_R'])
print(Data)
print("---------")

# Graficamos La función y el polinomio

F = sp.log(x**2+1)
ux = np.linspace(-2,5,500)
for i in [2,5,7]:
    P = serie_taylor(F, x0, i)
    print("Grado: ", i, "Polinomio: ", P)
    P = sp.lambdify(x, P)
    plt.plot(ux, P(ux), label=f"polinomio de grado: {i}")
    plt.legend()
    plt.xlabel("Eje X")
    plt.ylabel("Eje y")