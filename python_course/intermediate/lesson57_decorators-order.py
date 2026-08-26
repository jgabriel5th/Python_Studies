# Decorators order
def decoratorParameters(name):
    def decorator(func):
        print('Decorator:', name)

        def your_new_function(*args, **kwargs):
            res = func(*args, **kwargs)
            final = f'{res} {name}' # Concatenation
            return final
        return your_new_function
    return decorator



@decoratorParameters(name='fifth')
@decoratorParameters(name='fourth')
@decoratorParameters(name='third')
@decoratorParameters(name='second')
@decoratorParameters(name='first') 
def sumNumber(x, y):
    return x + y

ten_plus_five = sumNumber(10, 5)
print(ten_plus_five)