# polymorphism
# allows methods in different classes to share but do different functions
# theres also inheritance-polymorphism

class Animal:
    def speak(self):
        return 'sound'
    
class Cat:
    def speak(self):
        return 'meow'

class Bird:
    def speak(self):
        return 'tweet'

class Dog:
    def speak(self):
        return 'bark'

def sound(animal):
    print(animal.speak()) # prints the method from that parameter (class)

sound(Cat()) # meow
sound(Bird()) # tweet
sound(Dog()) # bark
print(Animal().speak()) # sound

# or call in a list, loop through every class's shared method
animals = [Cat(), Dog(), Bird()]

for animal in animals:
   print(animal.speak())

# Output:
# meow
# bark
# tweet