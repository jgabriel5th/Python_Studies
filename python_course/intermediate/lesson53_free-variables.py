# # Free variables + nonlocal (locals, globals)
# def out(x):
#     a = x # Free variable
#     def inside():
#         print(locals())
#         return a
#     return inside

# inside1 = out(10)
# inside2 = out(20)

# print(inside1())
# print(inside2())
def concatenate(start_string):
    final_value = start_string

    def intern(value_to_concatenate=''):
        nonlocal final_value # Used to avoid using final_value in this scope(intern) and using from concatenate's scope.
        final_value += value_to_concatenate
        return final_value
    return intern

c = concatenate('a')
print(c('b'))
print(c('c'))
print(c('d'))
print(final := c())