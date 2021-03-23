opc='s'
while(opc=='s' or opc=='S'):
    print("hoy haremos un programa de media aritmetica de la cantidad de numeros que usted desee")
    suma=0
    contador=0
    N=0
    while(N!=-1):
        N=0
        N=float(input("ingrese un numero, y cuando desee parar, ingrese el numero -1: "))
        while(N<-1):
            N=0
            print("Error, debe ingresar numeros mayores o iguales a -1")
            N=float(input("ingrese un numero, y cuando desee parar, ingrese el numero -1: "))
        suma=suma+N
        contador=contador+1
    if(N==-1):
       Media=suma/contador
       print("La media aritmetica de los valores ingresados es:",Media)        
       opc=input("desea repetir, ingrese (S/N)")
       while(opc!='s' and opc!='S' and opc!='n' and opc!='N'):
            print("Error, debe ingresar (S/N)")
            opc=input("desea repetir, ingrese (S/N)")
       if(opc=='N' or opc=='n'):
              print("Realizado por Catherine Betancurt Quintero Ingenieria en seguridad de la informacion")
