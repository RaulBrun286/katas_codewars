def repeats(numbers):
    
    i = 0
    result = 0
    
    for i in range(len(numbers)):
        if numbers.count(numbers[i]) == 1:
            result += numbers[i]
    return result