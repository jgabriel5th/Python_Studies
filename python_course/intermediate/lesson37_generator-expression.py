import sys

# Generator expression, Iterables and Iterators in Python
iterable = ['I', 'Have', '__iter__']
iterator = iter(iterable) # has __iter__ and __next__
list1 = [n for n in range(10000)]
generator = (n for n in range(10000)) # It's not tuple comprehension.

print(sys.getsizeof(list1)) # The whole list is already saved in memory: 85176B
print(sys.getsizeof(generator)) # It's quite similar to iterator, it knows the next value
# and will execute it only with next(): 200B

# for n in generator:
#     print(n)