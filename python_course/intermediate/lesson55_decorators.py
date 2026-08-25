# Decorators functions and decorators
# Decorate = Add / Remove / Restrict / Edit
# Decorator functions are function that decorate other functions.
# Decorators are used to make Python use decorator function in other functions.
# Decorators are "Syntax Sugar".
def createFunction(function): # Decorator function
    def intern(*args, **kwargs):
        print('I will decorate you')
        for arg in args:
            isString(arg)
        result = function(*args, **kwargs)
        print(f'Your result was {result}')
        print('You was decorated')
        return result
    return intern

@createFunction # Syntax Sugar
def reverse_string(string=str):
    print(f'{reverse_string.__name__}') # After Syntax Sugar, reverse_string will be changed by the return of createFunction's closure.
    return string[::-1]

def isString(parameter):
    if not isinstance(parameter, str):
        raise TypeError('Parameter must be a string')

reversed1 = reverse_string('Botafogo')
print(reversed1)