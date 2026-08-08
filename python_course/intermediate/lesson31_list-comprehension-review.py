# SYNTAX:
numbers = [1, 2, 3, 4, 5]
new_numbers = [number for number in numbers]

# new_numbers = []
# for number in numbers:
#     new_numbers.append(number)
print(numbers)
print(new_numbers)

##############################
# UTILIZATION:
def divisionFn(x, y):
    return x / y

def multiplicationFn(x, y):
    return x * y

def exponentiation(x, y):
    return x ** y

# division = [number / 2 for number in numbers] # Map
# multiplication = [number * 2 for number in numbers]
# square = [number ** 2 for number in numbers]

division = [divisionFn(number, 2) for number in numbers] # Using functions
multiplication = [multiplicationFn(number, 2) for number in numbers]
square = [exponentiation(number, 2) for number in numbers]

print(division)
print(multiplication)
print(square)

##############################
# FILTER:
numbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_numbers = [number for number in numbers2 if number > 5]
odd_numbers = [number for number in numbers2 if number % 2 != 0]
even_numbers = [number for number in numbers2 if number % 2 == 0]
another_if = [number if number != 6 else 600 for number in even_numbers]

print(numbers2)
print(new_numbers)
print(odd_numbers)
print(even_numbers)
print(another_if)

##############################
# ROWS AND COLUMNS:
# for x in range(1, 11):
#     for y in range(1, 6):
#         print(x, y)

rows_columns = [(x, y) if y != 2 else (x, y * 1000) for x in range(1, 11) for y in range(1, 6) if x != 2]
print(rows_columns)

##############################
# STRING:
string = 'João Gabriel'
new_string = ''.join([letter for letter in string]) # Using ''.join() will avoid the separated letters.
number_letters = 2
new_string2 = '.'.join([string[index:index + number_letters] for index in range(0, len(string), number_letters)])
print(new_string)
print(new_string2)

##############################
# NEW NAMES:
names = ['abraham', 'elícia', 'louise', 'john', 'mary']
new_names = [f'{name[:-1].lower()}{name[-1].upper()}' for name in names]
print(new_names)

##############################
# NUMBERS:
numbers = [[number, number ** 2] for number in range(10)]
flat = [y for x in numbers for y in x]
print(numbers)
print(flat)