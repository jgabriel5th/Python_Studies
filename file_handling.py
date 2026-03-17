'''
Learning file handling in Python.

Opening a file in Python:
- Python provides a built-in function named open() to open a file. It returns the file object that can be used to do several file operations later.
- Syntax to open the file: file_object = open(file_name, access_mode)

Definitions:
file_object is the variable or object that is going to accept and represent the file.
file_name is one of the parameters which will contain obviously the file name and its extension. It's possible to add the absolute path of the file.
access_mode is the way the file will be opened. There are three ways to acess the file: Read Mode, Write Mode and Append Mode.

Read Mode:
r - Read-only mode, file pointer placed at the beginning of the file, default mode.
rb - Reading only in binary format, file pointer at the beginning of the file as well.
r+ - Opens a file for reading and writing. File pointer at the beginning.
rb+ - Opens a file for reading and writing in binary format. File pointer at the beginning.

Write Mode:
w - Write-only mode. It will overwrite the file if the file exists, if not it will create a new one for writing.
wb - The same as "w" but binary.
w+ - Quite similar to "w", however it serves for writing and reading. if the file doesn't exist, it creates a new one for reading and writing.
wb+ - Also as w+, but binary.

Append Mode: differently from write mode that overwrite the existing file, the append mode will continue writing the data.
a - Opens a file for appending. The file pointer is at the end of the file if the file exists, if not it creates a new one for writing.
ab - The same as "a" but binary.
a+ - Similar  to "a", but for both appending and reading. If the file doesn't exist, it creates a new one for reading and writing.
ab+ - Basically a+ but binary.
'''
