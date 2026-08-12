# Dictionary Comprehension and Set Comprehension
product = {
    'name': 'Blue pen',
    'price': 2.5,
    'category': 'Office',
}

# for key, value in product.items():
#     print(key, value)
dictionary_comprehension = {
    key: value.upper()
    if isinstance(value, str) else value
    for key, value
    in product.items()
    if key == 'category'
}
print(dictionary_comprehension)

# list1 = [
#     ('a', 'value a'),
#     ('b', 'value b'),
#     ('c', 'value c'),
# ]
# # dc = {
# #     key: value
# #     for key, value in list1
# # }
# print(dc)

set_comprehension = {i for i in range(10)}
print(set_comprehension)