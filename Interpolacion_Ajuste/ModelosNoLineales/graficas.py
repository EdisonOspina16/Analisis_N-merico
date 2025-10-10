import matplotlib.pyplot as plt
import numpy as np

def graficas_transformaciones(x_data, y_data):

    plt.figure(figsize=(15,15), dpi=80)
    plt.suptitle('Transformación para linealizar Datos', fontsize=20)
    # Primera curva: datos originales
    plt.subplot(331)
    plt.plot(x_data, y_data, 'or', label='Datos originales')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Datos originales', fontweight='bold', fontsize= 8)

    # Segunda: Transformación # 1
    plt.subplot(332)
    plt.plot(x_data, y_data, 'mo')
    plt.xlabel('x')
    plt.ylabel('$\\sqrt{y}$')
    plt.title('Transformación Raíz de y', fontweight='bold', fontsize= 8)

    # Tercera: Transformación # 2
    plt.subplot(333)
    plt.plot(x_data, 1/y_data, 'go')
    plt.xlabel('x')
    plt.ylabel('$\\frac{1}{y}$')
    plt.title('Transformación $1/y$', fontweight='bold', fontsize= 8)

    # Cuarta: Transformación # 3
    plt.subplot(334)
    plt.plot(x_data**2, y_data, 'ko')
    plt.xlabel('$x^2$')
    plt.ylabel('y')
    plt.title('Transformación $x^2$', fontweight='bold', fontsize= 8)

    # Quinta: Transformación # 4
    plt.subplot(335)
    plt.plot(x_data**3, y_data, 'ko')
    plt.xlabel('$x^3$')
    plt.ylabel('y')
    plt.title('Transformación $x^3$', fontweight='bold', fontsize= 8)

    # Sexta: Transformación # 5
    plt.subplot(336)
    plt.plot(np.log(x_data), y_data, 'yo')
    plt.xlabel('$\\log(x)$')
    plt.ylabel('y')
    plt.title('Transformación $log(x)$', fontweight='bold', fontsize= 8)

    # Septima: Transformación # 6
    plt.subplot(337)
    plt.plot(x_data, np.log(y_data), 'co')
    plt.xlabel('x')
    plt.ylabel('$\\log(y)$')
    plt.title('Transformación $log(y)$', fontweight='bold', fontsize= 8)

    # Octava: Transformación # 7
    plt.subplot(338)
    plt.plot(np.sqrt(x_data), y_data, 'ko')
    plt.xlabel('$\\sqrt{x}$')
    plt.ylabel('y')
    plt.title('Transformación $log(y)$', fontweight='bold', fontsize= 8)

    # Nueve: Transformación # 8
    plt.subplot(339)
    plt.plot(np.log(x_data), np.log(y_data), 'go')
    plt.xlabel('$log(x)$')
    plt.ylabel('$log(y)$')
    plt.title('Transformación $log-log$', fontweight='bold', fontsize= 8)

    plt.tight_layout()
    plt.show()