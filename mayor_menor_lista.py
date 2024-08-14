def encontrar_minimo(lista):
    """ 
        Sirve para verificar que numero es el menor existente en una lista
        """
    if not lista:
        return None 
    minimo = lista[0]
    for numero in lista:
        if numero < minimo:
            minimo = numero
    
    return minimo

        



# Fin
print('\nEnontrar el valor minimo de una lista:')
print(encontrar_minimo([1, 5, 8, 3, 2]))
print(encontrar_minimo([-5, -10, -2, -1]))
print(encontrar_minimo([100, 0, 50, 75, 120, 25]))
        