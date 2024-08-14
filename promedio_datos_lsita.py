datos = [1, 2, 3, 4, 5]
suma = 0
i = 0
while i < len(datos):
    suma += datos[i]
    i += 1
promedio = suma / len(datos)

print("Con while:")
print(promedio)


datos = [1, 2, 3, 4, 5]
suma = 0
for numero in datos:

    suma += numero

promedio = suma / len(datos)
print("\nCon for:")
print(promedio)  # 3.0


def calcular_promedio(lista1, lista2):
    contador_suma = 0
    suma_cantidad = len(lista1) + len(lista2) 
    for numero in lista1:
        contador_suma += numero

    for numero in lista2:
        contador_suma += numero

    promedio_total = contador_suma / suma_cantidad 
    return promedio_total



# Fin
print('\nHallando promedios, sumando los numeros de dos listas')
print(calcular_promedio([1,2,3], [4,5,6]), ' <-Primer promedio')
print(calcular_promedio([1,2], [3,4]), ' <- Segundo promedio')


