# Local scopes
def my_func():
    my_var = 10 # Locally scoped to my_func, cant be used anywhere else
    print(my_var)

my_func() # 10

# print(my_var) # NameError: name 'my_var' is not defined
# Enclosed scopes
def outer_func():
    msg = 'Hello there!'
    res = ""  # Declare res in the enclosing scope

    def inner_func():
        nonlocal res  # Allows modification of an enclosed scope (res)
        res = 'How are you?'
        print(msg)  # Accessing msg from outer_func()

    inner_func()
    print(res)  # Now res is accessible and modified

outer_func()
# Output:
# Hello there!
# How are you?
# Global scopes
my_var1 = 10  # A global variable

def change_var():
    global my_var  # Allows modification of a global variable
    global my_var2
    my_var2 = 30
    my_var1 = 20

change_var()
# from global my_var2, it is now also accessible
print(my_var2)
print(my_var1) # my_var is now modified globally to 20