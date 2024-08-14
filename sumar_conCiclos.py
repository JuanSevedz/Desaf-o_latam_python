def sumar_datos(lista):
    """
        Funcion que sirve para sumar desde el segundo termino hasta el último
    """
    contador_suma = 0
    hasta = len(lista) - 1
    for numero in lista[1:hasta]:
        contador_suma += numero
    return contador_suma

# Fin
print('Summando desde-hasta:')
print(sumar_datos([4,6,8,2,3]))
print(sumar_datos([1,2,3,4,5,6,7,8]))
print(sumar_datos([10,11,12,13]))


def sumarPares(lista):
    """
        FUncion que sirve para sumar los nmero pares de una lista
    """
    contador_suma = 0
    for numero in lista:
        if numero % 2 == 0:
            contador_suma += numero

    return contador_suma



# Fin
print('\nSumando los pares:')
print(sumarPares([4,6,8,2,5]))
print(sumarPares([1,2,3,4,5,6,7]))
print(sumarPares([10,11,12,13]))