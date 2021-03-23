print("CALCULO DE RESISTENCIA EQUIVALENTE EN PARALELO")


N = input("Ingrese el número de resistencias en paralelo: ")
N = int(N)

suma = 0

for i in range(N):
    R = input("Ingrese el valor de la resistencia en Ohmios " + 
                str(i+1) + "/" + str(N) + ": ")
    R = float(R)
    # Calcular el inverso de cada resistencia
    suma = suma + 1/R

# Resistencia total en paralelo
Rt = 1/suma

print("La resistencia total de un circuito en paralelo de",
      N, "resistencias es: Rt =", Rt)
