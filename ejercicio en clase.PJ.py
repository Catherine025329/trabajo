# Determinar la cantidad de días de un mes ingresado por el usuario.

# Determinar la cantidad de días de un mes ingresado por el usuario.

# definir si el año es bisiesto o no

input("el año es bisiesto si o no: ")



def cantidad_dias(mes):
    if mes.lower() in ('enero', 'marzo', 'mayo', 'julio', 'agosto', 'octubre', 'diciembre'):
            return '31'

    elif mes.lower() == 'febrero':
         return '28'
     
     
    else: 
        return '30'

nombre_mes = input('Ingrese un mes: ')
