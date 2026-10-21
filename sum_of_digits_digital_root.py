def digital_root(numero):
    # El bucle se repite mientras el número tenga 2 o más cifras
    while numero >= 10:
        # Suma los dígitos del número actual
        numero = sum(int(digito) for digito in str(numero))

    return numero
