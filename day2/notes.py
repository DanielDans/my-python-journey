print(int('20'))
print(len('steps to python')) # it counts every char (space incl)
print(str(20)) # converts int to string
print(float(20)) # converts int to decimal

# input("Enter something: ")
print({'name': 'smartie'}['name']) # how dictionary works

# 'hello, world!' is an argument, one argument
print('hello', 'world!') # is 2 arguments, divided by different variables
# print can handle unlimited arguments, len handles 1
print(len('hello, world!'))

print(type(['Python', 'skating', 'playing']))
get_a_life = True
age = 14
person_info = {
    'name': 'smartie',
    'age': '14',
    'country': 'vn'
}
print(person_info['name'])
print(person_info['country'])
# [] brackets sometimes can be defined individually in a multiple value
# {} can work the same as """ i think
name2, age2, country2 = 'dumbie', '15', 'us'
# multiple variables in a line work in a way that defines variables to arguments in order
print(name2, age2, country2)
print('age: ', age)
print('country: ', person_info['country'])
print('info: ', person_info)
print('have a life?', get_a_life)

# input function gets user input, i learned this in class!!
age3 = input('Enter your age: ')
name3 = input('Enter your name: ')
print('your age is:', age3)
print('welcome,', name3)

# int to float
num_int = 12
print(num_int)
num_float = float(num_int)
print(num_float)

# float to int
num_float = 12.5
print(int(num_float))

# int to str
num_str = str(num_int)
print(num_str)

# str to int or float
num_str2 = '13.8'
num_float2 = float(num_str2)
num_int2 = int(num_float2)
print(num_int2)
print(float(num_str2))

# str to list
pi = '31415926535897932384626'
print(pi)
pi_list = list(pi)
print(pi_list) # lists every individual char

