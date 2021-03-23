 # Determinar la cantidad de días de un mes ingresado por el usuario.

# Determinar la cantidad de días de un mes ingresado por el usuario.

def cantidad_dias(mes):
    if mes.lower() in ('enero', 'marzo', 'mayo', 'julio', 'agosto', 'octubre', 'diciembre'):
            return '31'

    elif mes.lower() == 'febrero':
         return '28'
     
     
    else: 
        return '30'

nombre_mes = input('Ingrese un mes: ')


print("El Mes tiene", cantidad_dias(nombre_mes) + " días")
