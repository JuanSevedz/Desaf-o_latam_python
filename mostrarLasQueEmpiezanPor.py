def mostrarLasPalabrasQueEmpiezanConA(palabras):
    for palabra in palabras:
        if palabra.lower().startswith('a'):
            print(palabra)


# Fin
mostrarLasPalabrasQueEmpiezanConA(["manzana", "arándanos", "naranja", "pera", "uva"])
mostrarLasPalabrasQueEmpiezanConA(["gato", "perro", "ardilla", "pez", "conejo", "alce"])
mostrarLasPalabrasQueEmpiezanConA(["rojo", "azul", "verde", "amarillo"])