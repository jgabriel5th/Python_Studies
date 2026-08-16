# Understanding your own Python modules.
# The first executed module is called __main__
# It's possible to import a whole module or part of it.
# Python knows the folder where the __main__ is and below it.
# It doesn't recognize folders and modules above __main__ by default.
# Python knows all the modules and present packages on the ways of sys.path
try:
    import sys
    sys.path.append('/home')
except ModuleNotFoundError:
    ...
import lesson45_m

print('This module is called', __name__)
print(*sys.path, sep='\n')