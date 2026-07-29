'''
Exercise
Create a function that finds the first duplicated considering
the second number as the duplication. Return the duplication considered.
Requirements:
    The order of the duplicated number is considered from the second occurency
    of the number, which means, the duplicated number by itself.
    Example:
        [1, 2, 3, 3, 2, 1] -> 1, 2, 3 are duplicated (return 3)
        [1, 2, 3, 4, 5, 6] -> Return -1 (There are no duplicated ones)
    If none duplicated values in the list are found, return -1.
'''


list_of_lists_of_int = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

def firstDuplicated(list1):
    checkedNumbers = set()
    duplicatedNumber = -1
    for number in list1:
        if number in checkedNumbers: # True
            duplicatedNumber = number
            break
        checkedNumbers.add(number)
    return duplicatedNumber

for lists in list_of_lists_of_int:
    print(lists, firstDuplicated(lists))