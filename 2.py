#  Librerias usadas en el ejercicios
import random

#  Ejercicio 2
#  Area declaración de variables

cantidadNumeros=1
contadorRepeticiones=0
numero=0
acumuladorSumaTodosNumeros=0
acumuladorSumaNumerosPositivos=0
acumuladorSumaNumerosNegativos=0

#  Entradas
cantidadNumeros=int(input("Cantidad de Números: "))
#  Procesos
while contadorRepeticiones<cantidadNumeros:
    numero=random.randint(-100, 100)  #  Generamos número aleatorio
    print("numero : ",numero)
    acumuladorSumaTodosNumeros=acumuladorSumaTodosNumeros+numero # acumulo +
    if numero>0:
        acumuladorSumaNumerosPositivos=acumuladorSumaNumerosPositivos+numero
    else:
        acumuladorSumaNumerosNegativos=acumuladorSumaNumerosNegativos+numero
    contadorRepeticiones=contadorRepeticiones+1
#Fin del ciclo

#Salida de resultados
print("Suma todos: ", acumuladorSumaTodosNumeros)  
print("Suma positivos: ",acumuladorSumaNumerosPositivos)
print("Suma negativos: ",acumuladorSumaNumerosNegativos)  
    
    
    
    

