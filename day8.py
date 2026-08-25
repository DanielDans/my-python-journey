# 'for' loops
for i in [1, 2, 3]:
 # using list, the i doesnt need to be defined, it updates every loop till it reaches the last number
    print('bomb')

for i in range(3):
# works the same as above, with the parameter being the last number
    print('cheese')

print('bark\n' * 3, end='')
# \n seperates the string forforth into a new line
# multiplies will repeat the string
# end will make the end an empty string

while True: # keeps the loop if its body is true?
    n = int(input('type a positive num: '))
    if n < 0:
        continue # makes the loop ongoing
        print('number isnt positive')
    else:
        break # kills the loop
# This cycle can be abbreviated into:
# if n > 0:
# break
for i in range(n): # makes n the range
    print('complexity')
# variables defined in loops are accessible globally (unless in a func)

classmates = ['hanhan', 'gabe', 'david']
for student in classmates:
    print(student)
# prints every individual string in a list

print(classmates[1])
# sequences work differently when using brackets
# negative indexing accesses from end of the list

list(classmates[0])
# Lists every substring (letters) of the string

classmates[0] = 'feelings'
print(classmates[0])
# a specific value at an index can be updated

del classmates[2]
print(classmates)
# an element from a list can be deleted

work = ['programming', ['photography', 'drawing',]]
work[1][0] # gets the index inside a list thats an index of another

her, they, he = classmates
print(her)
# this is unpacking a list
close, *others = classmates
print(others)
# getting the rest of the list

desserts = ['Cake', 'Cookies', 'Ice Cream', 'Pie', 'Brownies']
desserts[1:4] # ['Cookies', 'Ice Cream', 'Pie']

classmates.append('kyen')
print(classmates)
# appends are for adding items to the list

other_classmates = ['ben', 'khoa']
classmates.extend(other_classmates)
# extends the list with another list