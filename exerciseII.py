
'''
Write a Python function to sum all the numbers in a list
'''
list = [8,2,3,0,7]
# def sumOfList(list):
#     sum = 0
#     for items in list:
#         sum = sum + items

#         return sum
# print(sumOfList(list))
#First attempt

def sumOfNumber(list):
    add = 0
    for items in list:
        add = add + items

    return add

print(sumOfNumber(list))