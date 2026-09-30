def multiTable(multiplicando):
    UNO = 1
    DIEZ = 10  
    tabla_de_multiplicar = ""
    for multiplicador in range(UNO, DIEZ + 1):
        tabla_de_multiplicar += (
            f"{multiplicador} * {multiplicando} = {multiplicador * multiplicando}\n"
        )
    return tabla_de_multiplicar[:-1]  # Remove the last newline character

print(multiTable(5))