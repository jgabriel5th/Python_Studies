# dir, hasattr and getattr in Python
# dir is used in debug console: variable -> dir(variable)
string = 'John'
method = 'upper'

if hasattr(string, method):
    print('Upper exists')
    print(getattr(string, method)())
else:
    print(f'It does not exist {method} method')