def duplicate_encode(word):
    word2 = word.lower()
    result = ""
    for letter in word2:
        if word2.count(letter) != 1:
            result += ")"
        else:
            result += "("
    return result
