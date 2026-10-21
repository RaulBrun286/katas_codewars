def multiTable(n):
    i = 1
    tabla = ""
    while i < 11:
        if i == 10:
            tabla += f"{i} * {n} = {i * n}"
        else:
            tabla += f"{i} * {n} = {i * n}\n"
        i += 1
    return tabla


print(multiTable(5))
