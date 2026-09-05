# classes (finally)
# class is a blueprint or template used to create objects
# attributes are like variables in a class meant to store data
# methods are functions defined in a class

class ClassName:
    def __init__(self, name, age):
        self.name = name # attribute
        self.age = age # attribute
    # class ClassName:
    # def __init__ is the special method thats called when a new object is created
    # the first parameter is always a reference to the object being created/used
    # it lets you access the objects own attributes and methods
    def sample_method(self): # method
        print(self.name.upper()) # what the method does

# these are objects, instances built from class
classname1 = ClassName('john', '14') # subject the variable to the class/make it the object
classname1.sample_method() # using the class's method

class Dog:
    species = 'ball' # class attribute

    def __init__(self, name, age):
        self.name = name # instance attribute
        self.age = age # instance attribute

    def bark(self):
        return f'{self.name} says woof, im {self.age} years old'

dog1 = Dog('Runner', '2')
dog2 = Dog('Crusher', '3')

print(dog1.bark())
print(dog2.bark())

print(dog1.species)
# instance attributes are unique to each object
# class attributes are shared between all instances


# special methods
# magic methods/dunder methods start and end w dbl underscores (__)

# arithmetic
# addition, __add__() is called, __sub__() for subtraction, __mul__() for multiplication, and __truediv__() for division.
# string operations
# __add__() is called for concatenation, __mul__() for repetition, __format__() for formatting, __str__() and __repr__() for text conversion, and so on.
# comparison
# __eq__() is called for equality checks, __lt__() for less-than, __gt__() for greater-than, and so on.
# iteration
# __iter__() is called to return an iterator and  __next__() to fetch the next item.

# these are meant for classes, regular len(), str() and so on doesnt work w the objects


class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __len__(self): 
        return self.pages
    # alters what len() does to the object
    def __str__(self):
        return f"'{self.title}' has {self.pages} pages"
    # does the same thing but for str()
    def __eq__(self, other):
        return self_pages == other.pages
    # changes how == operation works
book1 = Book('ZATO: I love the world and everything in it', '696')
book2 = Book('Milk inside a bag of milk inside a bag of milk', '420')

print(len(book1)) # 696
print(len(book2)) # 420
print(str(book1)) # 'ZATO: I love the world and everything in it' has 696 pages
print(str(book2)) # 'Milk inside a bag of milk inside a bag of milk' has 420 pages
print(book1 == book2) # False

class Cart:
    def __init__(self):
        self.items = [] # makes the object a list

    def add(self, item):
        self.items.append(item) # adds value to list

    def remove(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            print(f'{item} is not in cart')

    def list_items(self):
        return self.items # will return the list of items if method is used

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __contains__(self, item):
        return item in self.items

    def __iter__(self):
        return iter(self.items)