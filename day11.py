even_numbers = [num for num in range(21) if num % 2 == 0]
print(even_numbers)
# for each num in range, if num % 2 = 0, validate that as value
# i am quite confused
numbers = [1, 2, 3, 4, 5]
result = [(num, 'Even') if num % 2 == 0 else (num, 'Odd') for num in numbers]
print(result)
# the square brackets are like a placeholder for the function
# result will be num even if num % 2, else num odd will be next

enviroment = ['apartment', 'playground', 'sun', 'cloud', 'pool', 'field']
def big_word(word): # the function for filter, boolean based
    return len(word) > 4 # returns a boolean based on if len(word) > 4

new_enviroment = list(filter(big_word, enviroment))
# filter(function, iterable) makes the function take the iterable as parameter
# if function returns true, keep the word in the new list

celsius = [0, 10, 20, 30, 40]

def fahrenheitify(temp):
    return (temp * 9/5) + 32
# the function that converts C into F

fahrenheit = list(map(fahrenheitify, celsius))
# map(function, iterable) is like translate, puts the iterable through the function
# map also takes iterable for the function parameter

blazing_sun = sum(celsius, 10)
# sum(iterable, start) start is the initial value for summulation
# basically outputs the total of the iterable

lambda num: num ** 2
# lambda functions need a parameter, not in a nested bracket
# the function works after the double dot :

even = list(filter(lambda num: num % 2 == 0, numbers))
# kind of messy, but lambda doesnt need you to make a new func
# lambda also takes the iterable for parameter

# freeCodeCamp
def number_pattern(n):
    if not isinstance(n, int):
        return 'Argument must be an integer value.'
    if n < 1:
        return 'Argument must be an integer greater than 0.'
    return ' '.join([str(i) for i in range(1,n+1)])
print(number_pattern(13))