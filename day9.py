numbers = [10, 20, 30, 40, 50]
numbers.insert(1, 15)
# insert(index, object) puts object in list
print(numbers)

numbers.remove(50)
# remove takes value as argument to remove from list
print(numbers)
# only removes the first occurrence, not all

numbers.pop(1)
# pop(index) removes element at an index
# if not specified, remove the last

numbers.clear()
# wipes the entire list
print(numbers)

numbers = [2, 3, 7, 1, 1, 2, 8]
numbers.sort()
# sorts the list INSIDE THE VARIABLE

numbers.reverse()
# flips the order of the list

new_numbers = sorted(numbers)
# makes a new sorted list instead of modifying original list
# both sort() and sorted() accept optional key and reverse parameters

numbers.index(3)
# finds the index for the element in list

# tuple reviewing
# tuples are unmutable
menu = ('strawberry candy', 'olong tea', 'matcha squish')
# they were her favorite
face = 'soft'

menu[-2] # accessing an element, even with negative
# that was on her birthday

tuple(face) # makes a tuple out of the argument

'strawberry candy' in menu # checks if an element is in the tuple

# tuples can be unpacked with multiple variables
# also applys to *(variable) to get the rest of the tuple
# asterisks however create a list out of it
menu[1:3]
# she ate those a lot

menu.count(1)
# counts the number of an element in the list/tuple

menu.index(3)
# works the same way lists can