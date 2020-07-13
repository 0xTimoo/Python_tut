'''
Write a Python function to check whether a number is in a given range.
'''

x = int(input("What is the range of the number?"))
y = int(input("What is the range of the number?"))

def isInRange(n):
    if n < x:
        return "out of range"
    elif n > x and n < y:
        return "Value is in range"
    elif n > y:
        return 'out of range'
    return "Error"

n = int(input('INPUT A VALUE TO CHECK'))
print(isInRange(n))