def first_n_smallest(array, longitude):
    
    if len(array) == longitude:
        return array
    if longitude == 0:
        return []
    
    ordered_array = sorted(array)
    numbers_to_return = ordered_array[:longitude]
    final_list = []
    print(numbers_to_return)
    for number in array:
        if number in numbers_to_return:
            final_list.append(number)
            if final_list.count(number) > numbers_to_return.count(number):
                final_list.pop()
        if len(final_list) == longitude:
            break
    return final_list