def comp(array1, array2):

    if array1 is None or array2 is None or len(array1) != len(array2):
        return False

    sorter_array1 = sorted(
        x**2 for x in array1
    )  # Esto lo que hace es elevar al cuadrado todos los valores del array1
    sorter_array2 = sorted(array2)
    counter = 0

    for counter in range(0, len(array1)):
        if sorter_array1[counter] != sorter_array2[counter]:
            return False

    return True
