#Ejercicio 2:
# Puede ser que tengamos una función que recibe una cantidad fija de parámetros 
# y necesitemos llamarla enviando valores que se encuentran en una lista o tupla. 
# La forma más sencilla es anteceder el caracter * al nombre de la variable:
def sumar(v1, v2, v3):
    return v1 + v2 + v3

li=[2, 4, 5]
su=sumar(*li)
print(su) 
