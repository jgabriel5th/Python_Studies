# Understanding your own Python modules.
# The first executed module is called __main__
# It's possible to import a whole module or part of it.
# Python knows the folder where the __main__ is and below it.
# It doesn't recognize folders and modules above __main__ by default.
# Python knows all the modules and present packages on the ways of sys.path
import lesson45_m
from lesson45_m import soma, module_variable

print(lesson45_m.module_variable)
print(module_variable)
print(lesson45_m.soma(10, 34))
print(soma(300, 400))