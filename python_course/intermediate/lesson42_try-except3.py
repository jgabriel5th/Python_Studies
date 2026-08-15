# (Part 3) Try, except, ese and finally
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions
try: # try cannot be used alone.
    print('OPEN FILE')
    8 / 1
except ZeroDivisionError as e:
    print(e.__class__.__name__) # Used to catch the exception's name
    print(e)
    print('Divided by zero')
except IndexError as error:
    print('IndexError')
except (NameError, ImportError): # an except that handles two or more exceptions inside a tuple.
    print('NameError, ImportError')
else: # else will be executed if no exception is raised.
    print('Nothing has happened')
finally: # finally will be executed regardless if the exception is raised or not.
    print('CLOSE FILE')