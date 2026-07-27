'''
Useful dictionary methods in Python:
len - how many keys
keys - iterable with the keys
values - iterable with the values
items - iterable with keys and values
setdefault - add value if the key doesn't exist
copy - return a shallow copy
get - get a key
pop - deletes an item with the specified key(del) and return the value
popitem - deletes the last added item
update - updates a dictionary with another.
'''
p1 = {
    'name': 'Kyle',
    'last name': 'Crane',
    'height': 1.90,
}
# get()
print(p1.get('name')) # it avoids KeyError if the key doesn't exit differently from p1['age'].
print(p1.get('age')) # None(default)
print(p1.get('age', "It doesn't exist")) # It's possible to change the default(None) value.

# pop()
name = p1.pop('name') # name's value has gone to name variable.
print(name)
print(p1) # but was deleted from p1 dictionary.

# popitem()
last_key = p1.popitem() # it returns a tuple from the selected dictionary. The last key.
print(last_key)
print(p1) # And removes it from the dictionary.

# update() - literally updates the dictionary.
p1.update({ # first way
    'name':'Kyle',
    'age': 38,
})
p1.update(height=1.90) # keyword arguments - second way.
tuple1 = ('game', 'Dying Light'),
p1.update(tuple1) # tuple/list - third way
print(p1)