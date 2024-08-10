def cuadrado_hueco(n):
    for fila in range(n):
        if fila == 0 or fila == n - 1:
            # Imprime la primera y última fila completas con asteriscos
            print('*' * n)
        else:
            # Imprime las filas intermedias con asteriscos en los bordes y espacios en el centro
            print('*' + ' ' * (n - 2) + '*')


# Fin
cuadrado_hueco(4)
cuadrado_hueco(2)
cuadrado_hueco(6)
cuadrado_hueco(1)