# Exercise - Delaying function execution

# My attempt:
# def createAdder(adder):
#     def sumNumber(number):
#         return number + adder
#     return sumNumber

# def createMultiplier(multiplier):
#     def multiply(number):
#         return number * multiplier
#     return multiply

# sumByfive = createAdder(5)
# print(sumByfive(20))
# multiByten = createMultiplier(10)
# print(multiByten(10))


# Teacher's solution:
def sumNumber(x, y):
    return x + y

def multiply(x, y):
    return x * y

def createFunction(function, x):
    def intern(y):
        return function(x, y)
    return intern

sum_by_five = createFunction(sumNumber, 5)
multiply_by_ten = createFunction(multiply, 10)
print(sum_by_five(10))
print(multiply_by_ten(10))