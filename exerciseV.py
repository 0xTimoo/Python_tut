'''
Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
'''

def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)
        
x = int(input('what is the number you want to get it\'s factorial?'))
print(factorial(x)) 