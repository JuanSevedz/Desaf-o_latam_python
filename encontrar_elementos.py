def encontrar_indice(arreglo, elemento):
    # Escribe tu código aquí
    for i in range(len(arreglo)):
        if arreglo[i] == elemento:
            return i


    # Fin
    return None


print(encontrar_indice([1, 3, 5, 7, 9], 5))
print(encontrar_indice([1, 3, 5, 7, 9], 6))
print(encontrar_indice(["a", "b", "c"], "b"))


def buscar_stock(productos, stocks, producto_buscado):
    for i, producto in enumerate(productos):
        if producto == producto_buscado:
            return stocks[i]
    return None



# Fin
print('\nBuscar stock:')
print(buscar_stock(["manzana", "pera", "naranja", "uva"],[50, 30, 75, 20],"naranja"))

print(buscar_stock(["laptop", "celular", "tablet", "smartwatch"],[10, 50, 25, 15],"impresora"))