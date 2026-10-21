def duplicate_count(text):

    word = text.lower()
    abecedary = set(word)
    result = 0
    for letter in abecedary:
        if word.count(letter) > 1:
            result += 1
    return result
