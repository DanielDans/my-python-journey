# inheritance
# it is a subclass (child class) or another class
# it can use the attributes and methods of the parent class

class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return f'{self.name} makes a sound'

class Cat(Animal):
    meow = 'maow, murrph'

    def sound(self):
        base = super().sound() # holds the return value of parent method inside the variable
        return f'{base}, then {self.name} meows {self.meow}'
chrisymerchandez = Cat('Chris')
print(chrisymerchandez.sound()) # (without override) Chris makes a sound
print(chrisymerchandez.meow) # maow, mrrph
print(chrisymerchandez.sound()) # (after) Chris makes a sound. then meows maow, mrrph
# were able to use self.name attribute and sound method
# re-defing a method updates the method to do something for a specific subclass
class Tiger(Animal, Cat): # Inherits from a subclass
    def say(self):
        return f"Im {self.name} and i {self.meow}"

mike = Tiger('Mike')
print(mike.say()) # Im Mike and i maow mrrph