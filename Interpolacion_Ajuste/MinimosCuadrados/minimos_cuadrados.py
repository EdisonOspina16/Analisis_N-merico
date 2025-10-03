def minimos_cuadrados(x_data, y_data):
    n = len(x_data)
    sx = sum(x_data)
    sy = sum(y_data)
    sx_square = sum(x_data ** 2)
    syx = sum(y_data * x_data)
    m = (n * syx - sx * sy) / (n * sx_square - sx ** 2)
    b = (sx_square * sy - sx * syx) / (n * sx_square - sx ** 2)
    return m,b
