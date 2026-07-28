# Sets - type set
# Sets are taught in math.
# https://brasilescola.uol.com.br/matematica/conjunto.html
# They are graphically represented by the Venn diagram
# Sets in Python are mutable, however they accept only
# immutable types as inner values.


# Creating a set
# set(iterable) or {1, 2, 3} <- similar to dictionary but without the key.

# s0 = {} # <- This won't be an empty set but a dictionary.
s0 = set() # For empty set, the best way is with class set()
s1 = {'Luiz', 1, 2, 3}
print(s1, type(s1))


# Sets are efficient to remove duplicate iterable values.
# - they don't have indices;
# - they don't guarantee order;
# - they are iterable(for, in, not in)

# Useful methods:
# add, update, clear, discard