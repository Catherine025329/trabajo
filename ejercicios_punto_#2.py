#ejercicios punto 2

import pandas as pd


# Leer archivo excel

archivoexcel = pd.read_excel("C:/Users/Usuario/Desktop/COSAS EXCEL/POBLACIÓN Y AREA DEPART-COLOMBIA.xlsx")

# Imprimir los datos


# DESARROLLAR LO QUE NOS PIDEN

# 2.1 
area_total=0
cantidad_datos=0
area=archivoexcel["Area_km_al_cuad"]
for x in area:
    area_total = area_total + (x)
    cantidad_datos=cantidad_datos+1
print("2.1 el Area total de todo el país es: ",area_total+cantidad_datos-33)

#2.2 
suma_poblacion=0
numero_departamentos=0
poblacion=archivoexcel["Area_km_al_cuad"]
for x in poblacion:
    suma_poblacion = suma_poblacion + (x)
    numero_departamentos=numero_departamentos+1
   
print("2.2 el Promedio de Area x Departamento es: ",suma_poblacion/numero_departamentos)

#2.3 
menoramayor=archivoexcel.sort_values(by=['Poblation'],ascending=[True])
print("ORDEN DE MENOR A MAYOR Y VICEVERSA",menoramayor)


#2.5 
suma_poblacion=0
departamentos=0
poblacion=archivoexcel["Poblation"]
for x in poblacion:
    suma_poblacion = suma_poblacion + (x)
    departamentos=departamentos+1
   
print("2.5 el Promedio de población es: ",suma_poblacion/numero_departamentos)

#2.6
print("HABITANTES X KILÓMETRO AL CUADRADO: ")
print(area*poblacion)
