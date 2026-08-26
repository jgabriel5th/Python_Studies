'''
Considering two lists of integers or floats values (list A and list B).
Sum the values in the lists returning a new list with the summed values:

if a list is bigger than the other, the sum will only consider the length of the smaller
one.

'''
def sumList(list1, list2):
    sum_list = []
    for x, y in list(zip(list1, list2)):
        z = x + y
        sum_list.append(z)
    return sum_list

list_a = [1, 2, 3, 4, 5, 6, 7]
list_b = [1, 2, 3, 4]
sum_list = sumList(list_a, list_b)
print(sum_list)