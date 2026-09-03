test_settings = {
    'theme': 'light',
    'volume': 'high',
    'notifications': 'enabled'
}
def add_setting(settings_dict, settings_tuple):
    setting, value = settings_tuple
    setting = setting.lower()
    value = value.lower()

    if setting in settings_dict:
        return f"Setting '{setting}' already exists! Cannot add a new setting with this name."
    
    settings_dict[setting] = value
    return f"Setting '{setting}' added with value '{value}' successfully!"

def update_setting(settings_dict, settings_tuple):
    setting, value = settings_tuple
    setting = setting.lower()
    value = value.lower()

    if setting in settings_dict:
        settings_dict[setting] = value
        return f"Setting '{setting}' updated to '{value}' successfully!"
    else:
        return f"Setting '{setting}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings_dict, setting):
    setting = setting.lower()

    if setting in settings_dict:
        del settings_dict[setting]
        return f"Setting '{setting}' deleted successfully!"
    
    else:
        return 'Setting not found!'

def view_settings(settings_dict):
    if settings_dict == {}:
        return 'No settings available.'

    return 'Current User Settings:\n' + '\n'.join([f'{setting}: {value}'.capitalize() for setting, value in settings_dict.items()]) + '\n'

# certificate project!!

# error handling
# try, except, else, finally
try:
    x = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print("Division successful!")
finally:
    print('This block always runs')
# try is where the error will be anticipated
# except runs if the specificed error occurs
# else runs if no error occurs
# finally runs regardless of whether an error occurs or not
try:
    number = int('abc')
    result = 10 / number
except ValueError:
    print('That was not a valid number.')
except ZeroDivisionError:
    print("Can't divide by zero.")
# stacking these other than 'try' works

try:
    num = int(input("Enter a number: "))
    y = 1 / num
except (ValueError, ZeroDivisionError) as e:
    print(f'Error occurred: {e}')
# making e as alias will create an exception object that shows the error message
# stacking exceptions in a tuple is more readable

def check_num(numb):
    if numb < 0:
        raise ValueError("Number cant be negative")
    return numb
try:
    check_num(-5)
except ValueError as e:
    print(f'Error occurred: {e}') # Number cant be negative
# raise is used to explicitly trigger an exception

def process(data):
    try:
        info = int(data)
        return info * 2
    except ValueError:
        print('Put an integer')
        raise # re-raises the exception
try:
    process('abc')
except ValueError as e:
    print(f'Error occurred: {e}') # Put an integer
# raise (without arguments) will re-raise the exception thats being handled

# classes will create custom exceptions, but its for future lessions
def calculate_square_root(number):
    assert number >= 0, 'Cannot calculate square root of negative number'
    return number ** 0.5

try:
    result = calculate_square_root(-4)
except AssertionError as e:
    print(f'Assertion failed: {e}')
# assert is used to raise exceptions conditionally (AssertionError)