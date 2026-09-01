import os
# Creating files with Python
# It's used open function to open
# a Python file(it can exist or not)
# r(read), w(write), x(to creation)
# a(write in the end), b(binary)
# t(text mode), +(read and write)
# w - overwrite the file
# a - append something in the end of the file without overwriting it.

# Context manager - with(open and close)
# Useful methods
# write, read
# writelines(write several lines)
# seek(move the cursor)
# readline
# readlines

# os module:
# os.remove or unlink - removes a file
# os.rename - changes a file name or moves the file

# json module:
# json.dump = it generates a json file
# json.load
file_path = '/home/jgabriel5th/Desktop/Folder/'
file_path += 'file.txt'

# file = open(file_path, 'w') 
# #
# file.close() # The first thing after open() a file is to close() it.
# with open(file_path, 'w+') as file:
#    file.write('Line 1\n')
#    file.write('Line 2\n')
#    file.writelines(
#       ('Line 3\n', 'Line 4\n')
#    )
#    file.seek(0, 0)
#    print(file.read())
#    file.seek(0, 0)
#    print(file.readline().strip())
#    print('READLINES')
#    file.seek(0, 0)
#    for line in file.readlines():
#       print(line.strip()) 
# # with open(file_path, 'r') as file:
# #    print(file.read())

with open(file_path, 'w+', encoding='utf8') as file:
    file.write('Atenção\n')
    file.writelines(('Testing\n', 'Lines\n'))
    file.seek(0, 0)
    print(file.read())

with open(file_path, 'a+', encoding='utf8') as file:
    file.write('Appending')
    file.seek(0, 0)
    print(file.read())

# os.unlink(file_path) # os.remove() does the same, it removes the file.
# os.rename(file_path, 'file2.txt')