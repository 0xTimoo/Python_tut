'''
Write a Python program to reverse a string.
'''
def strReverse(string):
    reverseStr = string[::-1]
    return reverseStr
print(strReverse("1234abcd"))


#Method from w3resources
def string_reverse(string):

    rstring = ''
    index = len(string)
    while index > 0:
        rstring += string[ index - 1 ]
        index = index - 1
    return rstring
print(string_reverse('1234abcd'))