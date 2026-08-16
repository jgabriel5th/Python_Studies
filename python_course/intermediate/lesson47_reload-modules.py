import importlib

import lesson47_m # Modules in Python are singleton which mean it only exists one instance
# of it in the entire code. Once a module is imported, you can't import it again in the same program.

print(lesson47_m.variable)

for i in range(10):
    importlib.reload(lesson47_m)
    print(i)
    
print('Over')