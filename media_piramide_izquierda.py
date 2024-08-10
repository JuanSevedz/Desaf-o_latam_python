def media_piramide_izquierda(altura):
    for fila in range(1, altura + 1):
        # Calcula el número de espacios a imprimir antes de los asteriscos
        espacios = altura - fila
        # Imprime los espacios y luego los asteriscos
        print(' ' * espacios + '*' * fila)



# Fin
media_piramide_izquierda(4)
media_piramide_izquierda(2)
media_piramide_izquierda(1)
media_piramide_izquierda(6)
