# Packing and unpacking of dictionaries
a, b = 1, 2 # unpacking
a, b = b, a
# print(a, b)

person = {
    'name': 'Mary',
    'last name': 'Curie',
}
# a, b = person # It'll unpack dictionary's keys
# print(a, b) 

# x, y = person.values() # It'll unpack dictionary's values
# print(x, y)

# a0, b0 = person.items() # It'll unpack dictionary's items by returning them as tuples.
# print(a0, b0)

# (a1, a2), (b1, b2) = person.items() # It'll unpack but without the tuple, quite similar to enumerate().
# print(a1, a2)
# print(b1, b2)
# for key, value in person.items(): # Like this
#     print(key, value)


# How to unite dictionaries:
person1 = {
    'name': 'Sherlock',
    'last name': 'Holmes',
}

personal_data = {
    'age': 38,
    'height': 1.85,
}

completed_person = {**person, **personal_data} # ** serves to unpack.
# print(completed_person)

# args and kwargs
# args - positional arguments(non-named arguments)
# kwargs - keyword arguments(named arguments)

def showkeywordArguments(*args, **kwargs):
    print('NOT NAMED:', args)
    for key, value in kwargs.items():
        print(key, value)


showkeywordArguments(1, 2, 3, name='Louise', number=123)
showkeywordArguments(**completed_person)

settings = {
    'arg1':1,
    'arg2':2,
    'arg3':3,
    'arg4':4,
}
showkeywordArguments(**settings)