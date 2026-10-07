def create_phone_number(numeros):
    
    prefijo = str(numeros[0:3])
    primera_parte = str(numeros[3:6])
    segunda_parte = str(numeros[6:])
    
    telefono = f'({numeros[0]}{numeros[1]}{numeros[2]}) {numeros[3]}{numeros[4]}{numeros[5]}-{numeros[6]}{numeros[7]}{numeros[8]}{numeros[9]}'
    
    print(telefono)
    
    return telefono