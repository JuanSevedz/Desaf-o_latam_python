def primeros_x(lista, cantidad):
    lista_new = []
    for numero in lista[0:cantidad]:
        lista_new.append(numero)
    lista_new.sort()
    return lista_new

# Fin
print(primeros_x([7, 5, 3, 9, 1], 3)) 
print(primeros_x(["zorro", "elefante", "gato", "ballena"], 3))  
print(primeros_x([14, 3, 25, 8, 20], 4))  