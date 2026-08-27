schedule = ('math', 'science', 'english', 'literature', 'dominos pizza', 'english')
schedule.index('english', 3)
# index(value, indexstart, indexstop), value is what's searched for, index is where it starts
# adding another index as argument is the stop

sorted(schedule, key=len)
# this is using len to change sorting behavior from lowest words up

list(enumerate(schedule)) # [(0, 'subject'), (1, 'subject'), (2, 'subject')]
# enumerate() keeps track of each index for every iterable

languages = ['Spanish', 'English', 'Russian', 'Chinese']

for index, language in enumerate(languages):
    print(f'Index {index} and language {language}')
# loop variables can stack
# for's value (index, argument) of the enumerate are defined in its order
