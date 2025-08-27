import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sympy as sp


from Cota.cota_taylor import cota_taylor
from SeriesTaylor.serie_taylor import serie_taylor

#Defino la función
x = sp.symbols('x')
f = 3**(-x)
x0 = 1
n= 5

poly5 = serie_taylor(f,1,5)
print(f"El polinomio de Taylor de grado {n} es: {poly5}")

#Errores en x=1.5
P5_1_5 = poly5.evalf(subs={x:1.5})
f_1_5 = f.evalf(subs={x:1.5})
error_abs = abs(P5_1_5 - f_1_5)
error_rel = error_abs / abs(f_1_5)
print(f"Error absoluto en x=1.5: {error_abs}")
print(f"Error relativo en x=1.5: {error_rel}")

cota_R5_2 = cota_taylor(f, x0, 2, 5)
print(f"Cota del error R5(2): {cota_R5_2}")

#Gráfica
# Polinomios de diferentes grados
Poly1 = serie_taylor(f, x0, 1)
Poly2 = serie_taylor(f, x0, 2)
Poly4 = serie_taylor(f, x0, 4)
Poly6 = serie_taylor(f, x0, 6)

ux = np.linspace(0.5, 2, 400)
f_num = sp.lambdify(x, f, 'numpy')
P1_num = sp.lambdify(x, Poly1, 'numpy')
P2_num = sp.lambdify(x, Poly2, 'numpy')
P4_num = sp.lambdify(x, Poly4, 'numpy')
P6_num = sp.lambdify(x, Poly6, 'numpy')

plt.plot(ux, f_num(ux), label='f(x)')
plt.plot(ux, P1_num(ux), label='Taylor grado 1')
plt.plot(ux, P2_num(ux), label='Taylor grado 2')
plt.plot(ux, P4_num(ux), label='Taylor grado 4')
plt.plot(ux, P6_num(ux), label='Taylor grado 6')
plt.legend()
plt.title('Aproximaciones de Taylor para $3^{-x}$ en $x_0=1$')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()