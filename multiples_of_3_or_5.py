def solution(number):
    counter = 0
    result = 0
    if number <= 0:
        return 0
    else:
        for divisor in range(1, number):
            if divisor % 3 == 0 or divisor % 5 == 0:
                result = result + divisor
    return result