def permute_a_palindrome(word):

    word.upper()

    if len(word) == 0 or len(word) == word.count(word[0]):
        return True
    else:
        leter_list = set(word)
        odd_letter = 0

        for letter in leter_list:
            count = word.count(letter)
            if count % 2 != 0:
                odd_letter = odd_letter + 1
        if odd_letter <= 1:
            return True
        else:
            return False
