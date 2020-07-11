def maxOfTwo(x,y):
    if x >y:
        return x
    else: 
        return y
def maxOfThree(x,y,z):
    return maxOfTwo(x, maxOfTwo(y,z))


print(maxOfThree(1,4,67))
