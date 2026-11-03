def first_n_smallest(array, size):
    
    if len(array) == size:
        return array
    if size == 0:
        return []
    
    ordered_array = sorted(array)
    numbers_to_return = ordered_array[:size]
    final_list = []
    for number in array:
        if number in numbers_to_return:
            final_list.append(number)
            if final_list.count(number) > numbers_to_return.count(number):
                final_list.pop()
        if len(final_list) == size:
            break
    return final_list

if __name__ == "__main__":

    assert first_n_smallest([1, 2, 3, 4, 5], 3) == [1, 2, 3]
    assert first_n_smallest([5, 4, 3, 2, 1], 3) == [3, 2, 1]
    assert first_n_smallest([1, 2, 3, 1, 2], 3) == [1, 2, 1]
    assert first_n_smallest([1, 2, 3, -4, 0], 3) == [1, -4, 0]
    assert first_n_smallest([1, 2, 3, 4, 5], 0) == []
    assert first_n_smallest([1, 2, 3, 4, 5], 5) == [1, 2, 3, 4, 5]
    assert first_n_smallest([1, 2, 3, 4, 2], 4) == [1, 2, 3, 2]
    assert first_n_smallest([2, 1, 2, 3, 4, 2], 2) == [2, 1]
    assert first_n_smallest([2, 1, 2, 3, 4, 2], 3) == [2, 1, 2]
    assert first_n_smallest([2, 1, 2, 3, 4, 2], 4) == [2, 1, 2, 2]