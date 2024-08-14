mi_lista = [1, 2, 3, 4, 5]

auxiliar = mi_lista[1]
print(auxiliar)
mi_lista[1] = mi_lista[3]
print(mi_lista)
mi_lista[3] = auxiliar
print(mi_lista)



mi_lista = [1, 2, 3, 4, 5]
mi_lista[1], mi_lista[3] = mi_lista[3], mi_lista[1]

print('\n',mi_lista)  # [1, 4, 3, 2, 5]

def intercambiar_elementos(lista, cambio1, cambio2):
    lista[cambio1], lista[cambio2]= lista[cambio2], lista[cambio1]
    return lista


# Fin
print('\nDiciendo que valores cambiar:')
print(intercambiar_elementos([1, 2, 3, 4, 5], 0, 4))

print(intercambiar_elementos([10, 20, 30, 40, 50], 1, 3))

print(intercambiar_elementos(["rojo", "verde", "azul", "amarillo"], 0, 2))