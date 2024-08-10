def lineas_verticales_alternadas(filas, columnas):
    for fila in range(filas):
        linea = ''
        for columna in range(columnas):
            if (columna % 2 == 0):
                linea += '*'
            else:
                linea += ' '
        print(linea)



# Fin
lineas_verticales_alternadas(4,5)
lineas_verticales_alternadas(2,3)
lineas_verticales_alternadas(1,6)
lineas_verticales_alternadas(5,1)