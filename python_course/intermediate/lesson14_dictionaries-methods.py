'''
Useful dictionary methods in Python:
len - how many keys
keys - iterable with the keys
values - iterable with the values
items - iterable with keys and values
setdefault - add value if the key doesn't exist
copy - return a shallow copy
get - get a key
pop - deletes an item with the specified key (del)
popitem - deletes the last added item
update - updates a dictionary with another.
'''

cat = {
    'name': 'Newton',
    'breed': 'mixed',
}
cat.setdefault('age', None) # A way to put a default value in order to avoid an Exception.
print(cat['age'])
print(len(cat)) # 2 keys

print(list(cat.keys())) # It'll return dict_keys, in order to see it better it's necessary to convert
# to list or tuple first.
for key in cat.keys(): # The result will be the same if put the dictionary name.
    print(key)
for key in cat: # Recommended
    print(key)

print(list(cat.values())) # The same as keys(), but it'll return the values by creating dict_values.
for value in cat.values():
    print(value)

print(list(cat.items())) # The same as keys() and values() but it'll return both by creating dict_items.
# However it also will create a tuple.
for key, value in cat.items(): # similar to enumerate
    print(key, value)