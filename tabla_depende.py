def dibujar_tabla(n):
    numero = 1
    for fila in range(n):
        # Generar una línea con los números consecutivos
        linea = ''
        for columna in range(n):
            # Agregar el número actual a la línea con un espacio adicional para el formato
            linea += f'{numero:2} '
            numero += 1
        # Imprimir la línea completa
        print(linea.strip())


# Fin
dibujar_tabla(5)
dibujar_tabla(2)
dibujar_tabla(1)
dibujar_tabla(7)