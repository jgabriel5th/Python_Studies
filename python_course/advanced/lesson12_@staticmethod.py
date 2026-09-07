# @staticmethod is useless in Python(according to my course teacher)
# Static methods are methods that are within the class, but they don't
# have access to the self nor cls.
# Basically, they're functions that exist within the class.
class Class:
    @staticmethod
    def function_within_class(*args, **kwargs):
        print('HI', args, kwargs)

def function(*args, **kwargs):
    print('HI', args, kwargs)
    
c1 = Class()
c1.function_within_class(1, 2, 3)
Class.function_within_class(named=1)
function(1, 2, 3)
function(named=1)