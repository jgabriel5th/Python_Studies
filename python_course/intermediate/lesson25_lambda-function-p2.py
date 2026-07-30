def execute(function, *args):
    return function(*args)


# def sumNumbers(x, y):
#     return x + y


# def createMultiplier(multiplier):
#     def multiply(number):
#         return number * multiplier
#     return multiply

duplicate = execute(
    lambda m: lambda n: n * m, 2 # def parameter:(return) def parameter:(return) expression
)
print(duplicate(2))

print(
    execute(
        lambda x, y: x + y, 2, 3 # It's like: def parameters:(return) expression
    ),
    # execute(sumNumbers, 2, 3), # All of them are equivalent.
    # sumNumbers(2, 3)
)

# subNumber = lambda x, y: x - y # This is possible, however it's not recommended by PEP8.
# lambda should be executed inside another function and for simple things.

print(
    execute(
        lambda *args: sum(args), # lambda can also be used with *args
        1, 4, 45, 65, 31, 345
    )
)