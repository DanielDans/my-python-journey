# name mangling
class Parent:
    def __init__(self, internal='One', private='Two'):
        self._internal = internal
        self.__private = private

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__private = 'Child private'

object1 = Parent(
    'Accessible from outside, but should not',
    'Cant access anywhere outside'
    )
print(object1._internal) # Accessible from outside, but should not
# print(object1.__private) # AttributeError

print(object1.__dict__)
# {
#  '_internal': 'Accessible from outside, but should not',
#  '_Parent__private': 'Cant access anywhere outside'
# }
# Prefixing an attribute with __ internally renames the attribute to _ClassName__attribute
# __dict__ creates a dictionary containing the object's attributes
print(object1._Parent__private) # Cant access anywhere outside
# This means that accessing __ prefixes is possible via "Name Mangling"

object2 = Child()
print(object2.__dict__) # {'_internal': 'One', '_Parent__private': 'Two', '_Child__private': 'Child private'}