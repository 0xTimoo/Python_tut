'''
while loop

syntax

while <condition>:
    statement

'''


spam = 0
if spam < 5:
    print('Hello World.')
    spam += 1

while spam < 5:
    print('Hello World.')
    spam += 1

name  = ''
while True:
    print('Please type your name')
    name = input()
    if name == 'your name':
        break
print('Thank you!')

while True:
    print('who are you')
    name = input()
    if name != 'Joe':
        continue
    print(f'Hello  {name} What  is the password it is a fish')
    password = input()
    if password == 'Swordfish':
        break
print('Access Granted!')

'''
for loop syntax:

for <var_name> in <iterable>
iterable can be list, strings, dict, set, tuples and so on.

'''
print('My name is')
for i in range(5):
    pass
#    print('Jimmy Five times (' + str(i) + ')')

total = 0
for num in range(101):
    total += num
print(total)
 
for item in 'Timothy':
    print(item)

looping over dictionary

user = {
    'name' : 'Timothy',
    'age' : 22,
    'can_swim' : False
}
#printing all the item in the dict as tuple
for item in user.items():
    #key, value = item; using tuple unpacking
    print(key, value)
#printing the value
for item in user.values():
    print(item)
#printing the key
for item in user.keys():
    print(item)



Exercise

counter
my_list = [1,2,3,4,5,6,7,8,9,10]
total = 0
for i in my_list:
    total += i
print(total)


def  say_hello(name, emoji):
    print(f'Helloo {name} {emoji}')


say_hello('Timothy', ':)')


'''
parameters are when we create the function and create a parameters that will be in it, argument is the values that we provide when we are calling the function.

Good pratice for a Function: 
Function should do one thing really well;
Function should return something.


*args => argument
**kwargs => keyword argument


Rule: params, *args, default params, **kwargs  
'''

say_hello(emoji=':))', name='Timothy')

def sum(num1, num2) :
    def another_func(num1, num2):
        return num1 + num2
    return another_func(num1, num2)
    
total = sum(10,20)


print(total)


num = [20,13,12,18]

for i in num:
      pass

def  super_func(*args, **kwargs):
    print(args)
    print(kwargs)
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total

# print(super_func(1,2,3,4,5))
print(super_func(1,2,3,4,5,7, num1 = 3, num3=1))


def highest_even(li):
    even_list = []
    for i in li:
        if i % 2 == 0:
            even_list.append(i)
    return max(even_list)
print(highest_even([2,3,4,5,6,7,8,9,10]))
