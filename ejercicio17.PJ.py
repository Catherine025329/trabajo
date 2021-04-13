#Problema 1:
# Confeccionar una función que reciba el nombre de un operario, 
# el pago por hora y la cantidad de horas trabajadas. Debe mostrar su sueldo y el nombre. 
# Hacer la llamada de la función mediante argumentos nombrados.
def calcular_sueldo(nombre,costohora,cantidadhoras):
    sueldo=costohora*cantidadhoras
    print(nombre,"trabajo",cantidadhoras,"y cobra un sueldo de",sueldo)


# bloque principal

calcular_sueldo("juan",10,120)
calcular_sueldo(costohora=12,cantidadhoras=40,nombre="ana")
calcular_sueldo(cantidadhoras=90,nombre="luis",costohora=7) 
