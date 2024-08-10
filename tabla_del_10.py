def tabla_multiplicar():
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{i*j:3d}", end=" ")
        print()  # Nueva línea después de cada fila

# Llamada a la función
tabla_multiplicar()
