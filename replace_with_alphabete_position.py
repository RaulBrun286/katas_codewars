def alphabet_position(text):
    result =[]
        
    for letter in text:
        
        if letter.isalpha():
            
            result.append(str(ord(letter.upper())-64))
    return " ".join(result)