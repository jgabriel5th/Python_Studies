# Decorators with parameters
def decoratorsFactory(a=None, b=None, c=None):
    def functionFactory(func):
        print('Decorator 1')
        def nestled(*args, **kwargs):
            print(f'Decorator parameters: {[a, b, c]}')
            print('Nestled')
            res = func(*args, **kwargs)
            return res
        return nestled
    return functionFactory


@decoratorsFactory(1, 2 ,3)
def sumNumber(*args):
    total = 0
    for number in args:
        total += number
    return total

multiply = decoratorsFactory(1, 2, 3)(lambda x, y: x * y)

ten_plus_five = sumNumber(10, 5, 10, 20)
ten_times_five = multiply(10, 5)
print(ten_plus_five)
print(ten_times_five)