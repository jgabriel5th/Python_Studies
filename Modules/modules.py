'''
Reusability: reuse a particular code than developing a new one.
Python modules are used to do that.

Modules refer to a file containing Python statements and definitions.
Modules are also used to break down large programs into small manageable and organized files.
It's possible to define the most used functions in a module and import it, instead of copying them into different programs.
Examples of modules: Math and Random.

Types of Modules:
Built-in modules - They're available in Python by default, developed and maintained by the Python developer team.
It's possible to directly import them into to file, example: Math module.

Third-party modules -  They're similar to built-in modules, but they've got to be installed first. These modules can be installed using the 'pip' command.
PIP is a package manager for Python packages. They're uploaded and stored at the PyPI repository. PyPI = Python Package Index.

Syntax to download the third-party modules in the command-line/terminal.
Linux: pip3 install module_name
Windows: pip install module_name

Custom modules - They're the packages created by the developer, basically they are Python files which can be imported into another Python file/project.
When imported, it's possible to access their attributes and methods. These files files are called Python custom modules.


The three ways of using a Python module:

The import statement - To use a module, the first thing to do is import it using the import keyword, doing it will import the whole module into the Python project.
To use the function provided by the imported module it'll be necessary to use the dot(.) operator. 
Example: module_name.functionName() <- That's how an imported function will work.
Syntax to import: import module_name

Import statement and renaming - There are situations when the module's name is big, in order to solver this issue it's possible to rename a module while importing it.
The way to do it is using the import...as
Syntax: import module_name as a
- "a" is a new name given to this module, it could have been anything else. Therefore, instead of using module_name.functionName(), it would be a.functionName().

The from...import statement - It serves to import a particular attribute/function/class from a module, instead of the whole module.
Syntax: from module_name import functionName
Since it was imported only a particular attribute/function it isn't necessary to use the dort operator(.), the function can simply be called as shown below:
functionName()
'''

# Testing the three ways
import math 
print(math.factorial(4))

import math as m
print(m.sqrt(4))

from math import floor
print(floor(3.2))