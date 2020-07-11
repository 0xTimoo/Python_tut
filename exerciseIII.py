list = [8, 2, 3, -1, 7]
def multiplicationOfNumber(list):
    total = 1
    for items in list:
        total = total * items

    return total

print(multiplicationOfNumber(list))