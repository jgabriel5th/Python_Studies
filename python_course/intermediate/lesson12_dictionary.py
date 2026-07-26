# Dictionaries in Python (type dict)
# Dictionaries are data structures of the type pair of
# "key" and "value".
# Keys can be considered as the "index" saw in the lists
# and can be of immutable types such as: str, int, float, bool, tuple, etc.
# The value can be of any type, including other dictionary.
# It's used the keys - {} - or the class dict to create dictionaries.
# Immutables: str, int, float, bool, tuple.
# Mutable: dict, list.
person = {
    'name': 'John',
    'last name': 'Watson',
    'age': 42,
    'height': 1.72,
    'address': [
        {'boulevard': 'broken dreams', 'number': 123}
    ]
}
# person2 = dict(name='Thomas', last_name='Hobbes') # Second way to create a dict(unusual)
# print(person2)
print(person['name']) # Use [key_name] to access the key and see the value inside it.
print(person['last name'])

print()

for key in person:
    print(key, person[key]) # It'll print the key and the value in each iteration.
    