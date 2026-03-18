'''
Exception Handling: it's when the code is written right, but the user finds a way to break it.
As my professor says: "Don't trust the users, they'll always find a way to break the code."
Error: programming error is mainly known as bugs and the process to remove bugs from the program is called debugging.

Types of Errors:
Syntax Errors - Error in the source code of a program, any aspects of the code that do not conform to the syntax of the
chosen programming language will generate a syntax error. Also called compilation errors.
Logic Errors - They usually occur due to improper logic used in the program. They are difficult to debug.
Runtime Errors - Syntax and Logic are right, but for example: dividing any number by zero will result in a runtime error.

Exceptions:
Runtime Errors are called Exception, because the Syntax and Logic are right, but something or someone can cause an Exception.
Python provides ways for the developer to handle these Exceptions in order to avoid the program to crash.
This concept of handling Runtime Errors is named Exception Handling.

Examples of Exceptions:
- Division by Zero
- Value Error
- Addition of two incompatible types
- Accessing a nonexistent index of a sequence
- Opening a file that doesn't exist.

Benefits of Exception Handling:
- It makes your code more prepared for Exceptions.
- Therefore, it avoids the code to be broken.

Exception Class:
- It's the base class from which exceptions inherit.
- All the common built-in exceptions inherit from this class.

Common Exceptions:
StandardError - Base class for all built-in exception except StopIteration and SystemExit.
ArithmeticError - Numeric calculation errors.
FloatingPointError - When a floating-point calculation fails.
ZeroDivisionError - Division or modulo by zero happens.
EOFError - When there is no input from the the input() function and the end of the file is reached.
ImportError - When an import statement fails.
KeyboardInterrupt - When the user interrupts program execution, example: by pressing Ctrl+c.
IndexError - When an index is not found in a sequence.
NameError - When an identifier is not found in the local or global namespace.
IOError - When an input/output operation fails, for example print statement or open() when trying to open a file that doesn't exist.
SyntaxError - Error in Python syntax.
IndentationError - Error when indentation is not specified properly.
TypeError - When an operation or function is used with an invalid data type, a data that was not specified.
ValueError - When the built-in function's arguments have invalid values specified.
'''