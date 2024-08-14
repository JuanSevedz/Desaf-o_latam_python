def contar_numero(lista, numero):
    contador = 0
    for numeros in lista:
        if numeros == numero:
            contador += 1
    return contador



# Fin

print(contar_numero([1, 5, 3, 4, 5], 5))
print(contar_numero([1, 2, 3, 2, 4, 2], 2))
print(contar_numero([1, 2, 3, 4, 5], 6))