def comp(array1, array2):

    if array1 is None or array2 is None:
        return False
    if len(array1) == 0 and len(array2) == 0:
        return True
    if len(array1) != len(array2):
        return False
    sorter_array1 = sorted([number**2 for number in array1])  
    sorter_array2 = sorted(array2)

    position = 0
    for position in range(len(sorter_array1)):
        if sorter_array1[position] != sorter_array2[position]:
            return False

    return True

if __name__ == "__main__":
    a1 = [121, 144, 19, 161, 19, 144, 19, 11]
    a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
    assert comp(a1, a2) 
    a1 = [121, 144, 19, 161, 19, 144, 19, 11]
    a2 = [11*21, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
    assert comp(a1, a2) == False
    a1 = [121, 144, 19, 161, 19, 144, 19, 11]
    a2 = [11*11, 121*121, 144*144, 190*190, 161*161, 19*19, 144*144, 19*19]
    assert comp(a1, a2) == False
    a1 = [25, 74, 9]
    a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
    assert comp(a1, a2) == False
    a1 = []
    a2 = []
    assert comp(a1, a2) 
    a1 = None
    a2 = [1, 4, 9]
    assert comp(a1, a2) == False
    a1 = [1, 4, 9]
    a2 = None
    assert comp(a1, a2) == False
    
