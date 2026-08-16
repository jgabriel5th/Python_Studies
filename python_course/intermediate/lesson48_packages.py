from sys import path

# How to import a package:
import lesson48_package.modules # It'll come with namespace = lesson48_package.modules
from lesson48_package import modules # Namespace will be shorter = modules
from lesson48_package.modules import modules_sum # It'll import something without namespace.
from lesson48_package.modules import * # It'll import everything but it's bad coding practice.
# print(__name__) # __main__
print(*path, sep='\n')

print(modules_sum(1, 2))
print(lesson48_package.modules.modules_sum(20, 30))
print(modules.modules_multi(40, 30))
print(modules_divi(30, 0))