#Problema 1:
# Confeccionar una función que reciba entre 2 y n (siendo n = 2,3,4,5,6 etc.) valores enteros, retornar la suma de dichos parámetros.
def sumar(v1,v2,*lista):
    suma=v1+v2
    for x in range(len(lista)):
        suma=suma+lista[x]
    return suma


# bloque principal

print("La suma de 1+2")
print(sumar(1,2))
print("La suma de 1+2+3+4")
print(sumar(1,2,3,4))
print("La suma de 1+2+3+4+5+6+7+8+9+10")
print(sumar(1,2,3,4,5,6,7,8,9,10))
