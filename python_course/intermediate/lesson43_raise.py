# raise - raising exceptions (errors)
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions
def zeroDivision(x):
    if x == 0:
        raise ZeroDivisionError("You're trying to divide by zero")
    return True

def mustIntorFloat(x):
    type_x = type(x)
    if not isinstance(x, (float, int)):
        raise TypeError(
            f'"{x}" must be int or float.'
            f'"{type_x.__name__}" sent.'
        )
    return True

def divide(x, y):
    mustIntorFloat(x)
    mustIntorFloat(y)
    zeroDivision(y)
    return x / y

print(divide(8, 1))