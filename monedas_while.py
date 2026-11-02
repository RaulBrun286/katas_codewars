def euros(money):

    if type(money) is not int or money < 0:
        return None
    else:
        list_coins = [5, 2, 1]
        result = []
        rest = money
        counter = 0
        while rest > 0:
            i = list_coins[counter]
            result.append(rest // i)

            rest = rest % i
            counter += 1
        return tuple(result)

print(euros(8))
# >>> (1, 1, 1)  # una de 5 cénts, una de 2 cénts y una de 1 cént.
print(euros(5))
# >>> (1, 0, 0)  # una 5 cénts, ninguna de 2 cénts y ninguna de 1 cént.
print(euros(29))
# >>> (5, 2, 0)  # cinco de 5 cénts, dos de 2 cénts y ninguna de 1 cént.
print(euros(0))
# >>> (0, 0, 0) # ninguna de 5 cénts, ninguna de 2 cénts y 1 de cénts.
print(euros(170))
# >>> (34, 0, 0)  # treinta y cuatro de 5 cénts, ninguna de 2 cénts y ninguna de 1 cént.
print(euros(267))
# >>> (53, 1, 0)  # cincuenta y tres de 5 cénts, una de 2 cénts y ninguna de 1 cént.
print(euros(-2))
# >>> None
print(euros(5.576))
# >>> None
print(euros("5"))
# >>> None