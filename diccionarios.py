# Mostrar los obejtos del diccionario definidos en la función:
def presentar_diccionario():
    diccionario = {'nombre':'Juan','edad':25}
    return diccionario

# Fin
print(presentar_diccionario())


# Función para obtner un dato especificado:
def retornar_valor(diccionario, key1):
    valor = diccionario.get(key1)
    return valor
# Fin
print('\nObtener el valor que se especifica:')
print(retornar_valor({"nombre": "Juan", "edad": 25}, "nombre"))
print(retornar_valor({"nombre": "Juan", "edad": 25}, "edad"))



# Funcion para cambiar un valor especificado y mostrar todo el diccionario
def cambiar_valor(diccionario, key1, valor):
    diccionario[key1] = valor
    return diccionario


# Fin
print('\nDiccionario Editado:')
print(cambiar_valor({"nombre": "Juan", "edad": 25}, "nombre", "Pedro"))
print(cambiar_valor({"nombre": "Juan", "edad": 25}, "edad", 30))


# Funcion para tomar los valores de una lista y añadirlos a un diccionari en una llave especifica:
def agregar_cuenta(lista):
    suma_total = 0
    for elemento in lista:
        suma_total += elemento
    return {"cuenta": suma_total}

# Fin
print('\nValores en una llave específica:')
print(agregar_cuenta([1, 2, 3, 4, 5]))
print(agregar_cuenta([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(agregar_cuenta([]))




# Funcion para hallar el total de elementos que hay, seleccionando solo los valores -> .value()
# Se obtienen los valores del diccionario, lo convertimos en lista y se recorre para incrementar el contador
def encontrar_stock(diccionario):
    valores = diccionario.values()
    lista_valores = list(valores)
    suma = 0
    for i in lista_valores:
        suma += i
    return suma

# Fin
print(encontrar_stock({'manzanas': 50, 'peras': 30, 'naranjas': 75, 'uvas': 25}))
print(encontrar_stock({'laptop': 10, 'celular': 50, 'tablet': 25, 'smartwatch': 15}))




# Funcion para obtner el promedio de notas que hay en un diccionario
def calcular_promedio(diccionario):
    notas = diccionario.values()
    lista_notas = list(notas)
    suma = 0
    total_notas = len(notas)
    for i in lista_notas:
        suma += i
    return suma/total_notas
    
# Fin
print(calcular_promedio( {'Ana': 85, 'Luis': 90, 'María': 78, 'Juan': 92}))


# Funcion para contar la cantidad de productos que hay en un comercio:
def contar_productos(diccionario):
    Productos = diccionario.keys()# Extraemos las llaves
    lista_productos = list(Productos)# Creamos una lista que contenga las llaves que se extreyeron
    cantidad_productos = len(lista_productos)# se ve la longitud de la lista
    return cantidad_productos

# Fin
print(contar_productos({'manzanas': 50, 'peras': 30, 'naranjas': 75, 'uvas': 25}))
print(contar_productos({'laptop': 10, 'celular': 50, 'tablet': 25, 'smartwatch': 15, 'auriculares': 100}))