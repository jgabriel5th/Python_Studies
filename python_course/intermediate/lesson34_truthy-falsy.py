# Truthy and Falsy values, Mutable and Immutable types
# Mutable: [] {} set()
# Immutable: () "" 0 0.0 None False range(0, 10)
# Falsy values:
empty_list = []
empty_dictionary = {}
empty_set = set()
empty_tuple = ()
empty_string = ''
zero = 0
zero_float = 0.0
none = None
false = False
range1 = range(0)

def falsy(value):
    return 'falsy' if not value else 'truthy'

print(f'TESTE', falsy('TESTE'))
print(f'{empty_list=}', falsy(empty_list))
print(f'{empty_dictionary=}', falsy(empty_dictionary))
print(f'{empty_set=}', falsy(empty_set))
print(f'{empty_tuple=}', falsy(empty_tuple))
print(f'{empty_string=}', falsy(empty_string))
print(f'{zero=}', falsy(zero))
print(f'{zero_float=}', falsy(zero_float))
print(f'{none=}', falsy(none))
print(f'{false=}', falsy(false))
print(f'{range1=}', falsy(range1))