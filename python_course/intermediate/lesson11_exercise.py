# Exercises
# Create functions that duplicate, triplicate and quadruplicate
# the received number as parameter.

# def duplicate(number):
#     return number * 2

# def triplicate(number):
#     return number * 3

# def quadruplicate(number):
#     return number * 4 

# number = duplicate(5)
# number2 = triplicate(5)
# number3 = quadruplicate(5)
# print(number)
# print(number2)
# print(number3)

# Using closure:
def createMultiplier(multiplier):
    def multiply(number):
        return number * multiplier
    return multiply

duplicate = createMultiplier(2)
triplicate = createMultiplier(3)
quadruplicate = createMultiplier(4)
print(duplicate(3))
print(triplicate(9))
print(quadruplicate(10))

# Extra
def createDivider(divider):
    def divide(number):
        return number // divider
    return divide

divide2 = createDivider(8)
print(divide2(80))