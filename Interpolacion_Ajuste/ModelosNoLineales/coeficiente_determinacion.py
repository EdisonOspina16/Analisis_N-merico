import numpy as np

def coef_determinacion(m, b, x_data_trans, y_data_trans):
    linea = m * x_data_trans + b
    promedio = np.mean(y_data_trans)
    sum1 = sum((y_data_trans - linea)**2)
    sum2 = sum((y_data_trans - promedio)**2)
    rsquare = 1-sum1/sum2
    return rsquare
