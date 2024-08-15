# genera una lista por comprensión de los primeros x números multiplicados por 2, donde el valor de x es un parámetro de la función. 
def numeros_dobles(x):
    primeros_x_numeros = [i*2 for i in range(1, x+1)]
    return primeros_x_numeros



# Fin
print(numeros_dobles(3))
print(numeros_dobles(5))
print(numeros_dobles(10))

# Largo de los objetos -> string,en este caso que almacena la lista, esos valores del largo, los almacena en otra lista
def contar_largo(lista):
    return [len(string) for string in lista] 


# Fin
print(contar_largo(["hola", "python", "es", "genial"]))
print(contar_largo(["ejemplo 1", "texto de prueba", "otro caso"]))




# Filtrando palabra y creando la lista de las que cumplen la sentencia
def filtrar_palabras_cortas(lista):
    return [palabra for palabra in lista if len(palabra) > 3]


# Fin
print(filtrar_palabras_cortas(["casa", "sol", "gato", "en", "Python", "es", "divertido"]))
print(filtrar_palabras_cortas(["el", "perro", "come", "un", "hueso", "grande"]))
print(filtrar_palabras_cortas(["a", "ab", "abc", "abcd", "abcde"]))






# Funcion para verificar extension, añadirla y transformar a mayusculas una palabra
def procesar_palabras(lista):
    return [f"{palabra.upper()}-{len(palabra)}" for palabra in lista if len(palabra) > 3]

# Fin
print(procesar_palabras(["sol", "luna", "estrella", "planeta", "cometa", "galaxia"]))
print(procesar_palabras(["el", "perro", "come", "un", "hueso", "grande"]))
print(procesar_palabras(["a", "ab", "abc", "abcd", "abcde", "abcdef"]))



# Formando lista a partir de una lista de diccionarios, filtrando por una llave(key)
def obtener_titulos(lista):
    return [titulo['titulo'] for titulo in lista]


# Fin
print(obtener_titulos([{"titulo": "El principito", "autor": "Antoine de Saint-Exupéry"}, {"titulo": "Cien años de soledad", "autor": "Gabriel García Márquez"}, {"titulo": "1984", "autor": "George Orwell"}]))
print(obtener_titulos( [{"titulo": "Don Quijote", "autor": "Miguel de Cervantes"}, {"titulo": "Hamlet", "autor": "William Shakespeare"}]))
print(obtener_titulos([{"titulo": "La Odisea", "autor": "Homero"}, {"titulo": "Orgullo y prejuicio", "autor": "Jane Austen"}, {"titulo": "Crimen y castigo", "autor": "Fyodor Dostoevsky"}]))