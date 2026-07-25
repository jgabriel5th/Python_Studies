'''
Higher Order Functions(receive/return other functions) - First Class Functions(functions treated as other common data types(str, int, etc))
- Functions are data type in Python and it's possible to do several things with them
just like any other data type. Ex: assign a function into a variable, use it as argument or parameter, return it, etc.
'''

def greeting(msg, name):
    return f'{msg}, {name}!'

def execute(function, *args): # It's possible to pass function as arguments to other functions.
    return function(*args) # And return them.

# greeting_2 = greeting # greeting_2 is pointing to greeting() in the memory.

v = execute(greeting, "Good morning", 'John')
print(v)

print(
    execute(greeting,'Good afternoon', 'Newton')
)
print(
    execute(greeting,'Good evening', 'Oliver')
)