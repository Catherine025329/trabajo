print("ingrese 3 numeros enteros diferenetes")
e = int(input("elija 1 si lo quiere de mayor a menor y 2 si lo quiere de menor a mayor"))
a = int(input("ingrese el numero a"))
b = int(input("ingrese el numero b"))
c = int(input("ingrese el numero c"))

if (e == 1):    
    if (a > b):
        if (a > c):
            if(b > c):
               print(a, b, c)
            else:
               print(a, c, b)
    if (c > a):
        if (c > b):
            if(b > a):
               print(c, b, a)
            else:
               print(c, a, b)
    if (b > a):
        if (b > c):
            if(a > c):
               print(b, a, c)
            else:
               print(b, c, a)


if (e == 2):
    if (a < b):
        if (a < c):
            if(b < c):
               print(a, b, c)
            else:
               print(a, c, b)
    if (c < a):
        if (c < b):
            if(b < a):
               print(c, b, a)
            else:
               print(c, a, b)
    if (b < a):
        if (b < c):
            if(a < c):
               print(b, a, c)
            else:
               print(b, c, a)

if (a == b):
    print("b y a son iguales")
    if (a == c):
        print("a y c son iguales")
        if(b == c):
           print(" b y c con iguales")
           if(a == b == c):
              print("todos son iguales")
