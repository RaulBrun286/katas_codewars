def change_machine(money):

    if money is None or type(money) is not int:
        return None
    if money < 0:
        return None
    list_coins = [5, 2, 1]
    change = []
    restant_coins = money
    for coin in list_coins:
        change.append(restant_coins // coin)
        restant_coins = restant_coins % coin

    assert not restant_coins

    return tuple(change)


print(change_machine(8))
# >>> (1, 1, 1)  # una de 5 cénts, una de 2 cénts y una de 1 cént.
print(change_machine(5))
# >>> (1, 0, 0)  # una 5 cénts, ninguna de 2 cénts y ninguna de 1 cént.
print(change_machine(29))
# >>> (5, 2, 0)  # cinco de 5 cénts, dos de 2 cénts y ninguna de 1 cént.
print(change_machine(0))
# >>> (0, 0, 0) # ninguna de 5 cénts, ninguna de 2 cénts y 1 de cénts.
print(change_machine(170))
# >>> (34, 0, 0)  # treinta y cuatro de 5 cénts, ninguna de 2 cénts y ninguna de 1 cént.
print(change_machine(267))
# >>> (53, 1, 0)  # cincuenta y tres de 5 cénts, una de 2 cénts y ninguna de 1 cént.
print(change_machine(-2))
# >>> None
print(change_machine(5.576))
# >>> None
print(change_machine("5"))
# >>> None
print(change_machine(None))
# >>> None
