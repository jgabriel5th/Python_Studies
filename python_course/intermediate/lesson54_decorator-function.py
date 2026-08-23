# Decorators functions and decorators
# Decorate = Add / Remove / Restrict / Edit
# Decorator functions are function that decorate other functions.
# Decorators are used to make Python use decorator function in other functions.
def createFunction(function): # Decorator function
    def intern(*args, **kwargs):
        for arg in args:
            isString(arg)
        result = function(*args, **kwargs)
        print(f'Your result was {result}')
        return result
    return intern

def reverse_string(string=str):
    return string[::-1]

def isString(parameter):
    if not isinstance(parameter, str):
        raise TypeError('Parameter must be a string')

checkingParameter = createFunction(reverse_string)
reversed1 = checkingParameter('123')