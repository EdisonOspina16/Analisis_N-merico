from CerosDeFunciones.Biseccion.biseccion import biseccion
from CerosDeFunciones.PosicionFalsa.posicion_falsa import posicion_falsa

import numpy as np

tolerancia = 1e-8

funcion = lambda x: x**10-1
iteracion = posicion_falsa(funcion, 0, 3, tolerancia)
iteracion2 = biseccion(funcion, 0, 3, tolerancia)
print(iteracion, iteracion2)

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def posicion_falsa_animado(funcion, a, b, tolerancia):
    """
    Método de posición falsa con almacenamiento de datos para animación
    """
    if funcion(a) * funcion(b) >= 0:
        print("El intervalo no contiene una raíz.")
        return None, None

    # Listas para almacenar los datos de cada iteración
    iteraciones = []
    puntos_a = []
    puntos_b = []
    puntos_c = []
    valores_c = []

    iteracion = 0

    # Almacenar valores iniciales
    iteraciones.append(iteracion)
    puntos_a.append(a)
    puntos_b.append(b)

    # Calcular primer punto c
    c = b - funcion(b) * (a - b) / (funcion(a) - funcion(b))
    puntos_c.append(c)
    valores_c.append(funcion(c))

    while abs(funcion(c)) > tolerancia:
        iteracion += 1

        # Actualizar intervalo
        if funcion(a) * funcion(c) < 0:
            b = c
        else:
            a = c

        # Calcular nuevo punto c
        c = b - funcion(b) * (a - b) / (funcion(a) - funcion(b))

        # Almacenar datos de la iteración
        iteraciones.append(iteracion)
        puntos_a.append(a)
        puntos_b.append(b)
        puntos_c.append(c)
        valores_c.append(funcion(c))

    return (iteraciones, puntos_a, puntos_b, puntos_c, valores_c), (c, iteracion)


def f(x):
    """Función objetivo: x^10 - 1"""
    return x ** 10 - 1


# Parámetros del método
a_inicial = 0.5
b_inicial = 1.5
tolerancia = 1e-6

# Ejecutar el método y obtener los datos
datos, solucion = posicion_falsa_animado(f, a_inicial, b_inicial, tolerancia)

if datos is None:
    print("No se pudo encontrar una solución")
else:
    iteraciones, puntos_a, puntos_b, puntos_c, valores_c = datos
    c_final, num_iteraciones = solucion

    print(f"Raíz encontrada: {c_final:.8f}")
    print(f"Número de iteraciones: {num_iteraciones}")
    print(f"f({c_final:.8f}) = {f(c_final):.2e}")

    # Configurar la gráfica
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

    # Rango para graficar la función
    x = np.linspace(0.3, 1.7, 1000)
    y = f(x)

    # Gráfica superior: función y método
    ax1.plot(x, y, 'b-', linewidth=2, label='f(x) = x¹⁰ - 1')
    ax1.axhline(y=0, color='k', linestyle='--', alpha=0.5)
    ax1.grid(True, alpha=0.3)
    ax1.set_xlabel('x')
    ax1.set_ylabel('f(x)')
    ax1.set_title('Método de Posición Falsa - Convergencia a la raíz')
    ax1.legend()

    # Elementos que se actualizarán
    punto_a, = ax1.plot([], [], 'ro', markersize=8, label='Punto a')
    punto_b, = ax1.plot([], [], 'go', markersize=8, label='Punto b')
    punto_c, = ax1.plot([], [], 'mo', markersize=10, label='Punto c (aproximación)')
    linea_secante, = ax1.plot([], [], 'r--', linewidth=2, alpha=0.7, label='Línea secante')
    linea_vertical, = ax1.plot([], [], 'purple', linestyle=':', linewidth=2, alpha=0.7)

    ax1.legend(loc='upper right')

    # Gráfica inferior: convergencia del error
    ax2.set_xlabel('Iteración')
    ax2.set_ylabel('|f(c)|')
    ax2.set_title('Convergencia del Error')
    ax2.set_yscale('log')
    ax2.grid(True, alpha=0.3)

    linea_error, = ax2.plot([], [], 'b-o', linewidth=2, markersize=4)
    ax2.axhline(y=tolerancia, color='r', linestyle='--', alpha=0.7, label=f'Tolerancia = {tolerancia}')
    ax2.legend()

    # Texto para mostrar información
    texto_info = ax1.text(0.02, 0.98, '', transform=ax1.transAxes,
                          verticalalignment='top', fontsize=10,
                          bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))


    def animar(frame):
        if frame < len(iteraciones):
            # Obtener datos de la iteración actual
            a_actual = puntos_a[frame]
            b_actual = puntos_b[frame]
            c_actual = puntos_c[frame]
            fc_actual = valores_c[frame]

            # Actualizar puntos
            punto_a.set_data([a_actual], [f(a_actual)])
            punto_b.set_data([b_actual], [f(b_actual)])
            punto_c.set_data([c_actual], [fc_actual])

            # Actualizar línea secante
            x_secante = np.linspace(a_actual, b_actual, 100)
            # Ecuación de la recta secante: y = f(a) + (f(b)-f(a))/(b-a) * (x-a)
            y_secante = f(a_actual) + (f(b_actual) - f(a_actual)) / (b_actual - a_actual) * (x_secante - a_actual)
            linea_secante.set_data(x_secante, y_secante)

            # Línea vertical desde c hasta el eje x
            linea_vertical.set_data([c_actual, c_actual], [0, fc_actual])

            # Actualizar gráfica de convergencia
            if frame > 0:
                linea_error.set_data(iteraciones[:frame + 1], [abs(val) for val in valores_c[:frame + 1]])
                ax2.set_xlim(-0.5, max(5, iteraciones[frame] + 1))
                ax2.set_ylim(min(1e-10, min([abs(val) for val in valores_c[:frame + 1]]) * 0.1),
                             max([abs(val) for val in valores_c[:frame + 1]]) * 2)

            # Actualizar texto informativo
            texto_info.set_text(f'Iteración: {iteraciones[frame]}\n'
                                f'a = {a_actual:.6f}\n'
                                f'b = {b_actual:.6f}\n'
                                f'c = {c_actual:.6f}\n'
                                f'f(c) = {fc_actual:.2e}')

        return punto_a, punto_b, punto_c, linea_secante, linea_vertical, linea_error, texto_info


    # Crear y mostrar la animación
    anim = FuncAnimation(fig, animar, frames=len(iteraciones),
                         interval=1500, blit=False, repeat=True)

    plt.tight_layout()
    plt.show()

    # Opcional: guardar la animación como GIF
    # anim.save('posicion_falsa.gif', writer='pillow', fps=0.67)