# dictionaries
rating = {
    'math': 'ou shii',
    'science': 'hmm',
    'english': 'doesnt even need',
    'literature': ['just no', 'and no']
}

elements = dict([('gold', 'value'), ('iron', 'durable'), ('silver', 'shiny')])
# equivalent to one above, uses tuples. the above is more readable

rating['math'] = 'damnn' # 'ou shii' = 'damnn'
# this is how you access the value of a key-value pair
# you can also change the specific value of a key
rating.get('literature', []) # ['just no', 'and no']
# .get(key, default) returns the value of the key and you can set a default value incase it doesnt exist

rating.keys()
# dict_keys(['math', 'science', 'english', 'literature'])
rating.values()
# dict_values(['damnn', 'hmm', 'doesnt even need', ['just no', 'and no']])
# these get the keys and values for the dict
rating.items()
# gets the key-value pairs instead, but each pair in a tuple inside a list

rating.pop('english', 'doesnt even need')
# removes the key-value and returns its value
rating.popitem()
# removes the last inserted item

rating.update({ 'science': 'a bit hm', 'history': 'ez'} )
# updates the dict, if a key exists it overwrites its value, otherwise add the new dict in
for score in rating.values():
    print(score)
# values in a for loop, also works for .keys()

for subject, score in rating.items():
    print(subject, score)
# prints both key-value pair, only works with items()

products = {
    'Laptop': 990,
    'Smartphone': 600,
    'Tablet': 250,
    'Headphones': 70,
}

for product, price in products.items():
    products[product] = round(price * 0.8)
# for every key-value pair, key = discounted price
print(products)
# this loop changes the list

for score in enumerate(rating):
    print(score)
# gets the index and the key only
# put a .values() over the variable to iterate over them
for index, score in enumerate(rating.values(), 1):
    print(index, score)
# removes the brackets and commas tuples by adding a second loop variable to act as index
# .items() get tuples of key-value pairs entirely
# the number argument is the initial value of the count


# thas day 12!