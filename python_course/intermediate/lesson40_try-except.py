# (Part 1) Try, except, else and finally
try:
    a = 18
    b = 0
    c = a /  b
except ZeroDivisionError:
    print('Zero division')
except NameError:
    print('Name is not defined')
except (TypeError, IndexError): 
    print('TypeError + IndexError')
except Exception:
    print('ERRO DESCONHECIDO')

print('CONTINUE')