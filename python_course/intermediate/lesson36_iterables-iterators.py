# Generator expression, Iterables and Iterators in Python
iterable = ['I', 'Have', '__iter__']
iterator = iter(iterable) # has __iter__ and __next__
print(next(iterator)) # The only thing iterator knows is the next value.
print(next(iterator))
print(next(iterator)) 
# print(next(iterator)) # StopIteration exception
