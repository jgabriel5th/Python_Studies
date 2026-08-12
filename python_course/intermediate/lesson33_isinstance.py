# isinstance - used to know if an object is from a determined type.
list1 = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2), {0, 1}, {'name': 'John'},
    ]

for item in list1:
    if isinstance(item, str):
        print('STR')
        print(item.capitalize())

    elif isinstance(item, set):
        print('SET')
        item.add(5)
        print(item, isinstance(item, set))

    elif isinstance(item, (int, float)): # int, float == int or float
        print('NUM')
        print(item, item * 2)

    else:
        print('OUTRO')
        print(item)