def filtrar_mayores_a_diez(lista):
    mayores_de_10 = []
    for numero in lista:
        if numero > 10:
            mayores_de_10.append(numero)
    return mayores_de_10


# Fin
print('Filtar los mayores a 10')
print(filtrar_mayores_a_diez([8, 11, 15, 3, 20, 9, 10]))
print(filtrar_mayores_a_diez([1, 5, 12, 18, 2, 30, 10, 15]))

# Palabras que empienzan por una letra -> 'a'

def filtrar_palabras_con_a(lista):
    palabras = []
    for palabra in lista:
        if palabra[0] == 'a' or palabra[0] == 'A':
            palabras.append(palabra)
    return palabras



# Fin
print('\nPalabras que empiezan por "a-A":')
print(filtrar_palabras_con_a(["amigo", "banana", "casa", "Ala", "perro"]))
print(filtrar_palabras_con_a(["zapato", "árbol", "avión", "Azul", "rojo", "amarillo"]))


#Filtrando correos, especificamente los de gmail

def filtrar_correos_gmail(lista):
    gmail = []
    for correo in lista:
        if correo[-9:] == 'gmail.com':
            gmail.append(correo)
    return gmail


# Fin
print('\nCorreos de Gmail:')
print(filtrar_correos_gmail(["juan@gmail.com", "maria@hotmail.com", "pedro@gmail.com", "ana@yahoo.com"]))
print(filtrar_correos_gmail(["empresa@outlook.com", "soporte@gmail.com", "info@company.com", "contacto@gmail.com"]))

#Filtrar los que tienen cierta longitud(len)

def filtrar_datos_errados(lista):
    caracteres = [ ]
    for correcto in lista:
        if (len(correcto) == 8):
            caracteres.append(correcto)
    return caracteres

# Fin
print('\nSolo los que tienen extension de 8:')
print(filtrar_datos_errados(["00010000", "00000001", "100000000", "1100000010", "00000000", "00000001", "00000000", "100000010"]))
print(filtrar_datos_errados(["1010101", "11111111", "000", "00000000", "1111111111", "01010101"]))