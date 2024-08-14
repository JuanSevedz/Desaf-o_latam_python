def agregar_punto(notas):
    for i in range(len(notas)):
        notas[i] += 1
    print(notas)


# Fin
agregar_punto([2, 3, 4])
agregar_punto([5, 5, 6])


# Indicar la cantidad a adicionar a los elementos de la lista
def agregarStock(lista, numero):
    for i in range(len(lista)):
        lista[i] += numero
    return lista



# Fin
print('\nDiciendo cuanto agregar:')
print(agregarStock([2, 3, 4], 5))
print(agregarStock([5, 5, 6], 3))

# Capitalizar los nombres de una lista:
def capitalizar_nombres(nombres):
    """
    Capitaliza cada nombre en la lista `nombres` y retorna una nueva lista con los nombres capitalizados.

    Args:
    nombres (list of str): Lista de nombres en minúsculas.

    Returns:
    list of str: Nueva lista con los nombres capitalizados.
    """
    nombres_capitalizados = []
    for nombre in nombres:
        nombres_capitalizados.append(nombre.capitalize())
    return nombres_capitalizados


# Fin
print('\nAplicando capitalize a los elementos de la lista:')
print(capitalizar_nombres(["maria", "carlos", "ana", "pedro"]))
print(capitalizar_nombres(["juan", "lucia", "pablo", "luisa", "josefina"]))


# Editar y añadir cosas a los elementos que hay en la lista, modificandolos por posicion
def transformar(nombres):
    for i in range(len(nombres)):
        nombres[i] = nombres[i].strip().capitalize() + '.'
    return nombres




# Fin
nombres = [" ana", "luis ", " jose", "rosa", "julio "]
transformar(nombres)
print('\nAquí:',nombres)