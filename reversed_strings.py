def solution(string):
    i = -1
    resultado = ""
    while -i <= len(string):
        resultado += f"{string[i]}"
        i = i - 1
    return resultado