#Modificandola, su proceso....
def modificar_calificaciones(tupla):
    lista = list(tupla)
    if lista[0] < 70:
        lista[0] += 5
    if lista[-1] < 70:
        lista[-1] +=5
    nueva_tupla = tuple(lista) 
    return nueva_tupla

# Fin
print(modificar_calificaciones((65, 80, 75, 90, 60)))
print(modificar_calificaciones((75, 80, 85, 90, 95)))