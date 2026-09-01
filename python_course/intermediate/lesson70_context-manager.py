# Creating files with Python
# It's used open function to open
# a Python file(it can exist or not)
# r(read), w(write), x(to creation)
# a(write in the end), b(binary)
# t(text mode), +(read and write)

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
with open(file_path, 'w') as file:
    print('Hello world')
    print('Your file will be closed')