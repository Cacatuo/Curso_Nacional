# Potencia base para referir todo a pu
Pbase = 1
# numero de barras del sistema
num_barras = 4
# numero de lineas del sistema
num_lineas = 5
# datos de las barras
# bus | demanda | gmin | gmax
# bus: nombre del bus (debe ser unico)
# demanda: potencia activa del nodo demandada
# gen min: generación mínima en el nodo (>=0)
# gen max: generación máxima del nodo (>=0)
datos_bus = [[1, 0.0, 0.0, 1.05],
             [2, 0.60, 0.0, 0],
             [3, 0.20, 0.0, 0.0],
             [4, 0.25,0.0,0.0]]

# datos de las lineas
# bus_i | bus_j | n0 | nmax| X | cap | costo
# bus_i: bus de envío de la línea
# bus_j: bus de recibo de la línea
# n0: numero de circuitos activos caso base
# nmax: número máximo de circuitos en paralelo
# X: reactancia [pu] de los circuitos
# cap: Potencia máxima por cada circuito
# costo: costo de construcción de un nuevo circuito

datos_lineas = [
    [1, 2, 0, 2, 3, 0.35, 3],
    [1, 3, 1, 2, 2, 0.40, 2],
    [1, 4, 0, 2, 2, 0.40, 2],
    [2, 4, 0, 2, 2, 0.40, 2],
    [2, 3, 1, 3, 2, 0.40, 2]
]