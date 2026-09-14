# Encapsulation
# Attributes only accessible from inside

# 1 underscore is internal access
class Wallet:
    def __init__(self, balance):
        self.__balance = balance # makes balance available for internal use only

    def __validate(self, amount): # you can define private methods
        if amount < 0:
            raise ValueError('Amount must be positive!')

    def deposit(self, amount):
        self.__validate(amount)
        self.__balance += amount # add to balance safely

    def withdraw(self, amount):
        self.__validate(amount)
        if amount > self.__balance:
            raise ValueError('Insufficient')
        self.__balance -= amount # remove from balance safely

    def get_balance(self):
        return self.__balance
# 2 underscore is private to the class only
# cant be accessed outside

account = Wallet(500)
# print(account.__balance) # AttributeError

# if you wanted to get __balance, define a method that returns it
print(account.get_balance()) # 500

# Getters and Setters
# Controls how attributes are accessed and modified, done through "properties"
# Mainly runs extra logic behind get, set, delete values; manipulating data within objecs

class Square:
    def __init__(self, side):
        self._side = side

    @property
    def area(self):
        return self._side * 4

    # GETTER
    @property # decorator, applying changes to a function without changing the code
    def find_side(self):
        return self._side # is a getter (accessible)

    # SETTER
    @find_side.setter # .setter makes a setter for the property
    def find_side(self, value): # value is the given parameter
        if value <= 0:
            raise ValueError('Side has to be positive')
        self._side = value # returns self._side as the new given parameter

    # DELETER
    @find_side.deleter
    def find_side(self):
        print('Deleting side')
        del self._side

my_square = Square(4)

print(my_square.area) # 16
print(my_square.find_side) # 4 | this calls the GETTER
my_square.find_side = 6 # modifies the value into given number | this calls the SETTER
print(my_square.find_side) # 6

del my_square.find_side # this calls the DELETER

try:
    print(my_square.find_side)
except AttributeError as e:
    print(f'Error:', e) # Error: 'Square' object has no attributes '_side' 

# properties let you use only dot notations
# always use underscore "_attribute" when using them inside setters or RecursionError
