articulo_a=0
articulo_b=0
total_a=0
total_b=0

articulo_a=input("ingrese el código del artículo a: ")
articulo_b=input("ingrese el código del artículo b: ")

codigo_articulo_a=articulo_a[-1]
codigo_articulo_b=articulo_b[-1]

if codigo_articulo_a == "x" and codigo_articulo_b == "x":
    precio_unitario=int(input("ingrese el precio unitario: "))
    numero_articulos=int(input("ingrese el numero de articulo: "))
