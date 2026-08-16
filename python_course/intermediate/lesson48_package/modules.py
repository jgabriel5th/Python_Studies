__all__ = [ # Used to limit imported things by from package.modules_name import *
    'modules_divi',
]

def modules_sum(x, y):
    return x + y

def modules_sub(x, y):
    return x - y

def modules_multi(x, y):
    return x * y

def zeroDivision(y):
    if y == 0:
        raise ZeroDivisionError('You are trying to divide by zero')
    return True

def modules_divi(x, y):
    zeroDivision(y)
    return x / y