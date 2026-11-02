def up_array(initial_number):
    # 1. Validar si la lista está vacía o si contiene elementos inválidos (no enteros o fuera de rango)
    if not initial_number:
        return None
        
    for check in initial_number:
        # Verificamos que sea un entero estricto y que esté entre 0 y 9
        if type(check) is not int or check > 9 or check < 0:
            return None
    
    # 2. Convertir a cadena de texto para procesar la operación
    transform = "".join(map(str, initial_number))
    
    # 3. Sumar 1 al número entero
    suma = int(transform) + 1
    
    # 4. Convertir de nuevo a texto manteniendo la longitud original con ceros a la izquierda
    # .zfill() asegura que si el original medía 3 caracteres, el nuevo mida mínimo 3 caracteres
    longitud_original = len(initial_number)
    resultado_str = str(suma).zfill(longitud_original)
    
    # 5. Devolver la lista convertida a enteros individuales
    return [int(x) for x in resultado_str]