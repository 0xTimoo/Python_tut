iq = 100
user_age = iq / 5

# augmented assignment operator
 
Name = 'Timothy'
age = 22

print('hi {name}. You are {age} years old.'.format(name = 'Tobi', age=19))

print(f'hi {Name} You are {age} years old')


Username = input('What is your username? ')
password = input('What is your password? ')

passlen = len(password)
print(f'{Username}, Your password is ' + '*' * len(password)  + f' {passlen} letter long')

print(passlen)

age = int(input('How old are you? '))
is_licenced = bool(input('Are you lisenced? '))

if age >= 18 and is_licenced:
    print('You arr allowed to drive!')
elif age < 18:
    print('you are not up to 18')
else:
    print('You are not allowed to drive')

ternary operator

condition_if_true if condition else condition_if_else

condition = "message" if condition=True 


is_magician = True
is_expert = True

# check if magician and expert:

if is_magician and is_expert:
    print('You are a master')
elif is_magician or is_expert:
    print('You are getting there')
elif not is_magician:
    print('you need magic power')


a = [1,2,3]
b = [1,2,3]

print(a==b)
print(a is b)

LOOPS
FOR LOOP

