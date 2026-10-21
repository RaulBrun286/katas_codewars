def first_dup(word):

    for letter in word:
        if word.count(letter) > 1:
            return letter
    return None
