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
import copy # module to use copy.deepcopy()

d1 = {
    'k1': 1,
    'k2': 2,
}
d2 = d1 # It doesn't copy like it happens with immutable data, it points
# to the same dictionary(d1) in the memory.
d2['k1'] = 1000
# print(d1) # d1 was edited by d2


# Shallow copy: copies all the immutable data but not mutable data(list or dictionaries.)
d3 = {
    'k3': 3,
    'k4': 4,
    'l1': [0, 1, 2],
}
d4 = d3.copy() # d4 made a shallow copy of d3
d4['k5'] = 5
print(d3) 
print(d4) # Both d3 and d4 have a list though the immutable data is different now.


# Deep copy: copies both immutable and mutable data.
# copy.copy() <- works just like shallow copy
d5 = {
    'k6': 6,
    'k7': 7,
    'l2': [3, 4, 5],
}
d6 = copy.deepcopy(d5) # d6 has made a deepcopy of d5
d6['l2'][0] = 30
d6['l3'] = [40]
print(d5)
print(d6) # Now d6 doesn't affect d5.