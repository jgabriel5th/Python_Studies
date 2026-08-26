# Exercise - Merge lists
# Create a zipper function (as clothes zipper)
# This function's utility is to merge two lists in order.
# Use all the values from the smallest list.
# Ex.:
# ['Salvador', 'Brasilia', 'Belo Horizonte']
# ['BA', 'DF', 'MG', 'SP']
# Result:
# [('Salvador', 'BA'), ('Brasilia', 'DF'), ('Belo Horizonte', 'MG')]

# def zipper(x, y):
#     max_range = min(len(x), len(y))
#     return [(x[i], y[i]) for i in range(max_range)]
# print(zipper(cities, states))
from itertools import zip_longest

cities = ['Salvador', 'Brasilia', 'Belo Horizonte']
states = ['BA', 'DF', 'MG', 'SP']
print(list(zip(cities, states))) # Python already has a native zip function.
print(list(zip_longest(cities, states, fillvalue='NO CITY')))