def juntarPalabras(lista):
    palabras = ''
    for palabra in lista:
        palabra = palabra + ' '
        palabras = palabras + palabra
    return palabras

# Fin 
print('Primer ejercicio:')
print(juntarPalabras(["Buenos", "días", "a", "todos"]))
print(juntarPalabras(["Vamos", "a", "comenzar"]))
print(juntarPalabras(["Yo", "soy", "tu", "padre"]))

# Escribe tu código aquí 
def mensajeOculto(lista):
    mensaje = ""  
    for palabra in lista:
        mensaje += palabra[0]  
    return mensaje



# Fin 
print('\nMensjae OcUlTo:')
print(mensajeOculto(["Gallina", "Abeja", "Tigre", "Oso"]))
print(mensajeOculto(["Música", "Isla", "Sol", "Tren", "Elefante", "Ratón", "Iguana","Oso"]))
print(mensajeOculto(["Luna", "Loro", "Avión", "Vaca", "Elefante"]))


def mensajeOculto2(lista):
    mensaje = "" 
    for i in range(len(lista)):
        if i % 2 == 0:
            if lista[i]:
                mensaje += lista[i][0]
    return mensaje



# Fin 
print('\nMensaje oculto pero solo las posiciones pares:')
print(mensajeOculto2(["Tronco", "Perro", "Oso", "Gato", "Perro", "Loro", "Onda"]))
print(mensajeOculto2(["Sol", "Oso", "Elefante", "Lana", "Casa", "Perro", "Rana", "Gato", "Estrella", "Cuerda", "Tigre"]))
print(mensajeOculto2(["Luna", "Loro", "Avión", "Vaca", "Nutria", "Oso", "Arbol"]))
