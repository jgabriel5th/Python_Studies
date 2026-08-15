# Built-in Python modules (import, from, as and *)
# https://docs.python.org/3/py-modindex.html

# Ways to import modules:

# whole - import module_name
# Advantages: you've got the module's namespace 
# Disadvantages: big names
# import sys
# sys. <- this is the namespace
# platform = f'My platform is: {sys.platform}'
# print(platform)

# parts - from module_name import object1, object2
# Advantages: small names
# Disadvantages: No module's namespace
# from sys import exit, platform
# platform = "Something" # Doing this will overwrite module's variable since it doesn't have namespace.
# print(platform)

# alias 1 - import module_name as surname <- change module name
# import sys as s # It's recommended not do this.
# sys = 'Anything' # And change variable's name to something else instead.
# print(s.platform)
# print(sys)

# alias 2 - from module_name import object as surname <- change module's object name
# from sys import exit as ex
# from sys import platform as pf
# print(pf)

# Advantages: it's possible to reserve names for the code.
# Disadvantages: you might be outside language pattern.

# bad coding practice - from module_name import *
# Advantages: imports everything from a module
# Disadvantages: imports everything from a module without namespace
