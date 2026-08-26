'''
Considering two lists of integers or floats values (list A and list B).
Sum the values in the lists returning a new list with the summed values:

if a list is bigger than the other, the sum will only consider the length of the smaller
one.

'''
from itertools import zip_longest

def sumList(list1, list2): # First way
    sum_list = [x + y for x, y in zip(list1, list2)]
    return sum_list

list_a = [1, 2, 3, 4, 5, 6, 7]
list_b = [1, 2, 3, 4]
sum_list = sumList(list_a, list_b)
print(sum_list)

sum_list2 = []
for i in range(len(list_b)): # Second way
    sum_list2.append(list_a[i] + list_b[i])
print(sum_list2)

sum_list3 = [x + y for x, y in zip_longest(list_a, list_b, fillvalue=0)] # Third way
print(sum_list3)