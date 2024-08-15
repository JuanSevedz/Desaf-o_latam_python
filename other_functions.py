# Poniendo en practica el concepto de las variables globales/Locales


# 1.De forma local
def saludar():
    mensaje = "Hola, mundo!"
    print(mensaje)


def otro_saludo():
    mensaje = "Alcance local"
    print(mensaje)


saludar()
otro_saludo()

# 2.De forma global -> se usa 'global <<variable>>'
total = 1000


def actualizar_total(cantidad):
    # Escribe tu código aquí
    global total

    # Fin
    total += cantidad
    print(f"El total actual es: {total}")


actualizar_total(500)
actualizar_total(-200)


def concatenar_strings(*args):
    """
    Función para tomar los argumentos que el usuario esta ingresando y convertirlos en una frase.
    """
    return " ".join(args)

    # Fin
    pass


print(concatenar_strings("Hola", "mundo"))
print(concatenar_strings("Python", "es", "genial"))


# Funcion para sobre escribir valores de diccionarios
def configurar_base_datos(**kwargs):
    # Valores predeterminados
    configuracion = {
        "host": "localhost",
        "puerto": 3306,
        "usuario": "root",
        "contraseña": "",
        "nombre_bd": "mi_app",
    }

    # Actualizar los valores predeterminados con los argumentos proporcionados
    configuracion.update(kwargs)

    return configuracion


# Fin

print(configurar_base_datos(puerto=5432, usuario="admin", nombre_bd="proyecto1"))
print(configurar_base_datos(host="192.168.1.1", contraseña="secreto"))
print(configurar_base_datos())


print("\n*" + "*" * 29, "Funciones lambada", "*" * 30)
# Funciones Lambda


def concatenador(valor1, valor2):
    # Define un lambda para concatenar los valores
    suma = lambda v1, v2: v1 + "-" + v2
    # Utiliza el lambda y retorna el resultado
    return suma(valor1, valor2)


# Fin
print(concatenador("Hola", "mundo"))
print(concatenador("Hola", "amigo"))


# Funcion sqrt() del módulo math
import math


def calcular_raices(lista):
    lista_raices = []
    for numero in lista:
        raiz = math.sqrt(numero)
        lista_raices.append(raiz)
    return lista_raices


# Fin
print(calcular_raices([4, 9, 16, 25]))
print(calcular_raices([4, 9, 16, 25, 36]))


# Funcion map para reccorrer listas y cambiar sus elementos
def formatear_nombres(lista):
    resultado_map = map(str.capitalize, lista)
    lista_formateada = list(resultado_map)
    return lista_formateada


# Fin
print(formatear_nombres(["ANA", "juan", "MaRia", "CARLOS"]))
print(formatear_nombres(["PEDRO", "luisa", "FernAnDO", "sofia"]))
print(formatear_nombres(["jULIA", "MARTIN", "alejandro", "CARMEN"]))


# Fucionando lambda y map
def corregir_nombre(lista):
    resultados = map(lambda str: str.strip().capitalize(), lista)
    resultados = list(resultados)
    return resultados


# Fin

print(corregir_nombre(["juan", " ana", "pedro "]))
print(corregir_nombre([" maría ", "josé", " luis"]))
print(corregir_nombre(["CARLOS", "sofía ", " elena"]))


# combinando la funcion filter -> Solo devueleve los objetos que cumplen la condición
# Se combina el filter con lambda


def filtrar_mayores_que(lista, limite):
    filtro = filter(lambda x: x > limite, lista)
    rsultado_lista = list(filtro)
    return rsultado_lista


# Fin
print(filtrar_mayores_que([1, 5, 10, 15, 20], 10))
print(filtrar_mayores_que([-5, 0, 5, 10, 15], 0))
print(filtrar_mayores_que([100, 200, 300, 400, 500], 250))


# funcion reduce del modulo functools combinado con lambda para que haga un ciclo de la funcion que se indica sobre elementos de una lista

from functools import reduce


def calcular_producto(lista):
    producto = reduce(lambda x, y: x * y, lista)
    return producto


# Fin
print(calcular_producto([1, 2, 3, 4, 5]))
print(calcular_producto([2, 3, 4]))
print(calcular_producto([1, 10, 100]))
