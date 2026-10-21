def array_diff(a, b):

    result = []
    for number in a:
        if number not in b:
            result.append(number)
    return result
