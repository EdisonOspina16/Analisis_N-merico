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

P1 = serie_taylor(f, x0, 1)
P5 = serie_taylor(f, x0, 5)
P8 = serie_taylor(f, x0, 8)

# Convertir a funciones numéricas (para graficar con numpy)
f_num = sp.lambdify(x, f, 'numpy')
P1_num = sp.lambdify(x, P1, 'numpy')
P5_num = sp.lambdify(x, P5, 'numpy')
P8_num = sp.lambdify(x, P8, 'numpy')

ux = np.linspace(0.1, 3, 400)
Y_f = f_num(ux)
Y_P1 = P1_num(ux)
Y_P5 = P5_num(ux)
Y_P8 = P8_num(ux)

plt.figure(figsize=(9,6))
plt.plot(ux, Y_f, 'r-', linewidth=2, label='f(x) = exp(x)/x')
plt.plot(ux, Y_P1, 'g--', linewidth=1.5, label='Taylor grado 1')
plt.plot(ux, Y_P5, 'b--', linewidth=1.5, label='Taylor grado 5')
plt.plot(ux, Y_P8, 'm--', linewidth=1.5, label='Taylor grado 8')

plt.axvline(x=1, color='gray', linestyle=':', label='Centro x0=1')
plt.title("Aproximación de f(x) con Polinomios de Taylor (grados 1, 5, 8)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()