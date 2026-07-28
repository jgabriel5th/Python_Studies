# # Sets - type set
# # Sets are taught in math.
# # https://brasilescola.uol.com.br/matematica/conjunto.htm
# # They are graphically represented by the Venn diagram
# # Sets in Python are mutable, however they accept only
# # immutable types as inner values.


# # Creating a set
# # set(iterable) or {1, 2, 3} <- similar to dictionary but without the key.

# # s0 = {} # <- This won't be an empty set but a dictionary.
# # s0 = set() # For empty set, the best way is with class set()
# # s1 = {'Luiz', 1, 2, 3}
# # print(s1, type(s1))


# # Sets are efficient to remove duplicate iterable values.
# # - their values always are unique;
# # - they don't accept mutable values;
# # - they don't have indices;
# # - they don't guarantee order;
# # - they are iterable(for, in, not in)
# l1 = [1, 2, 3, 3, 3, 3, 3, 1]
# s1 = set(l1)
# l2 = list(s1)
# print(s1) # Eliminated duplicated values in l1 list by type conversion.
# s2 = {1, 2.3, 'John', (123,)} # Only immutable data
# print(1 in s2) # Find an item inside a set.
# for item in s2:
#     print(item)

# # Useful methods:
# # add, update, clear, discard
# s1 = set()
# s1.add('John') # This method allows to add one element at a time in a set.
# s1.add(5)
# s1.update(('Green', 1, 2, 3, 4)) # This methods allows to add more than one element, but it'll return
# # the data in the iterable form, so it's necessary to put for example them in tuple() to solve. Otherwise, it'll
# # iterate each element.
# # s1.clear() # it clears the set
# s1.discard('Green') # it discards a specified value from a set.
# s1.discard('John')
# print(s1)

# # Useful operators:
# # union | - Unites
# # intersection & - Common items in both sets.
# # difference - Present items only on the left set.
# # Simetric difference ^ - Items which aren't in both sets.
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2 # Output: {1, 2, 3, 4} - They were united
s3 = s1 & s2 # Output: {2, 3} - Values in common
s3 = s1 - s2 # Output: {1} - s1 has 1 as an unique value and s1 is on the left.
s3 = s2 - s1 # Output: {4} - s2 has 4 as an unique value and now is on the left.
s3 = s1 ^ s2 # Output: {1, 4} - It shows all unique values regardless the set.
print(s3)