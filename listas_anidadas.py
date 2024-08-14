# Recooriendolas y almacenandolas en otra lista pra mostrar:
def mostrar_elementos(lista_compras):
    elementos = []
    for categoria in lista_compras:
        elementos.extend(categoria)
    print("...".join(elementos))


# Fin
mostrar_elementos(
    [["Tomates", "Lechuga", "Pepinos"], ["Pollo", "Pescado"], ["Arroz", "Pasta"]]
)
mostrar_elementos(
    [["Manzanas", "Peras"], ["Leche"], ["Pan", "Tortillas", "Croissants", "Bagels"]]
)


# Esto muestra correctamente los elementos en las posiciones donde tanto el índice de la fila como el índice de la columna son pares.
def imprimir_posiciones_pares(lista):
    for elementos in range(len(lista)):
        for elemento in range(len(lista[elementos])):
            if elementos % 2 == 0 and elemento % 2 == 0:
                print(f"({elementos}, {elemento}) {lista[elementos][elemento]}")


# Fin
print("\nEjercicio2:")
imprimir_posiciones_pares([["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]])
imprimir_posiciones_pares([["1", "2"], ["3", "4"], ["5", "6"], ["7", "8"]])


# Este codigo busca el objeto que se indica entre las sublistas y retorna la posicion, si la encuentra:
def encontrar_palabra(lista, palabra):
    for i, sublista in enumerate(lista):
        for j, elemento in enumerate(sublista):
            if elemento == palabra:
                return (i, j)
    return None


# Fin
print(
    encontrar_palabra(
        [
            ["gato", "perro", "ratón"],
            ["manzana", "banana", "cereza"],
            ["rojo", "verde", "azul"],
        ],
        "verde",
    )
)
print(encontrar_palabra([["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]], "j"))


# Esta funcion cuenta y retorna la cantidad de elementos que contienen las sublistas:
def contar_por_categoria(lista_compras):
    conteos = []
    for categoria in lista_compras:
        conteos.append(len(categoria))
    return conteos


# Fin
print(
    contar_por_categoria(
        [["Tomates", "Lechuga", "Pepinos"], ["Pollo", "Pescado"], ["Arroz", "Pasta"]]
    )
)
print(
    contar_por_categoria(
        [["Manzanas", "Peras"], ["Leche"], ["Pan", "Tortillas", "Croissants", "Bagels"]]
    )
)


# Esta función verifica si existe una lista anidada en la lista que se recibe como parámetro:
def tiene_lista_anidada(lista):
    for elementos in lista:
        if isinstance(elementos, list):
            return True
    return False
# Fin
print('\nHay una lista anidada:')
print(tiene_lista_anidada([1, 2, 3, 4, 5]))
print(tiene_lista_anidada([1, [2, 3], 4, 5]))



# Función que sirve para sumar los elementos que se encuentran dentro de la lista anidada:
def sumar_lista_anidada(lista):
    suma = 0
    for elementos in lista:
        for elemento in elementos:
            suma += elemento
    return suma


# Fin
print('\nLa suma de los valores de las listas dentro de la ista es: ')
print(sumar_lista_anidada([[1, 2], [3, 4]]))
print(sumar_lista_anidada([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))



