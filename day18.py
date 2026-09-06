# dynamic attribute handling
# getattr(), setattr(), hasattr(), and delattr()

# getattr(object, attribute_name, default_value)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person('Lincoln', 40)

attr_name = input('Enter attribute to see: ')
print
print(getattr(person, attr_name, 'Attribute not found'))
# prints the default value if attribute doesnt exist in class

print(getattr(person, 'name')) # Lincoln
print(getattr(person, 'age')) # 40
print(getattr(person, 'city', 'Washington')) # Washington
# Washington is a defauly value because 'city' doesnt exist in the class

# dir() returns a list of all attribute names on the object
# dir() returns everything from the object actually
for attr in dir(person):
    # ignores dunder methods
    if not attr.startswith('__') and not callable(getattr(person, attr)):
        # callable() returns a boolean if the object can be called like a method
        value = getattr(person, attr)
        print(f'{attr}: {value}')


# setattr(object, attribute_name, value)
# allows you to create a new attribute or update an existing one
# note: this sets attributes INTO OBJECTS

class Configuration:
    pass

# data loaded at runtime
settings_data = {
    'server_url': 'https:/slashapi.example.com',
    'timeout_s': 30,
    'retries': 5
}

config_obj = Configuration()

# dynamically set attributes using dict keys-value
for attr_name, attr_value in settings_data.items():
    setattr(config_obj, attr_name, attr_value)

print(config_obj.server_url) # https:/slashapi.example.com
print(config_obj.timeout_s) # 30
# settings_data's values are now attributes of config_obj


# hasattr(object, attribute_name)
# returns a boolean based on its existence

neccessities = ['name', 'age', 'gender']

for attr in neccessities:
    if not hasattr(person, attr):
        print(f'Missing attribute: "{attr}"')
    else:
        # access it dynamically once existence is confirmed
        print(f'{attr}: {getattr(person, attr)}')
# output:
# name: Lincoln
# age: 40
# Missing attribute: "gender"


# delattr(object, attribute_name)

# removed attributes
remove = ['timeout_s', 'retries']

# dynamically removes it
for attr in remove:
    if hasattr(config_obj, attr): # checks if attr is in object
        delattr(config_obj, attr)
        print(f'Removed: {attr}')

# loop through remaining attributes with dir()
for attr in dir(config_obj):
    if not attr.startswith('__') and not callable(getattr(config_obj, attr)):
        print(f'Remaining attribites: {getattr(config_obj, attr)}')

# freeCodeCamp
class MusicalInstrument:
    def __init__(self, name, instrument_type):
        self.name = name
        self.instrument_type = instrument_type

    def play(self):
        print(f'The {self.name} is fun to play!')

    def get_fact(self):
        return f'The {self.name} is part of the {self.instrument_type} family of instruments.'

instrument_1 = MusicalInstrument('Oboe', 'woodwind')
instrument_2 = MusicalInstrument('Trumpet', 'brass')

instrument_1.play()
print(instrument_1.get_fact())

instrument_2.play()
print(instrument_2.get_fact())