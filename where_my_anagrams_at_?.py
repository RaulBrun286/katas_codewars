def anagrams(word, words):

    result = []
    # sorted ordena las letras de la palabra en orden alphabetico
    order_word = sorted(word)

    for check in words:
        if order_word == sorted(check):
            result.append(check)
        else:
            continue
    return result
