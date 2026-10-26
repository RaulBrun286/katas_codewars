def grille(message, code):
    # 1. Convertimos el código a binario sin prefijo
    binary = format(code, "b")

    # 2. Rellenamos con ceros si el binario es más corto que el mensaje
    final_code = binary.zfill(len(message))

    # 3. ¡EL PASO CLAVE! Si el binario es más largo que el mensaje,
    # nos quedamos únicamente con los últimos caracteres (alineación a la derecha)
    if len(final_code) > len(message):
        final_code = final_code[-len(message) :]

    final_message = list(message)

    result = []
    for counter in range(0, len(message)):
        if final_code[counter] == "1":
            result.append(final_message[counter])

    return "".join(result)
