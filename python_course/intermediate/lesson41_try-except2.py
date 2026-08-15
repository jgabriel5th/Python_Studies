# (Part 2) Try, except, else and finally
try:
    # print('Line 3'[10])
    a = 18
    b = 0
    c = a / b
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
except NameError:
    print('Name is not defined')
except (TypeError, IndexError) as error: # Exceptions should be handled individually, not like this <--
    print('TypeError + IndexError')
    print('MSG:', error)
    print('Name:', error.__class__.__name__)
except Exception:
    print('ERRO DESCONHECIDO')

print('CONTINUE')