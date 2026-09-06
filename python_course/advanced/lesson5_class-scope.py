# Class scope and class methods
class Animal:
    # name = 'Lion' # class scope

    def __init__(self, name):
        self.name = name
        variable = 'value'
        print(variable)

    def eat(self, food):
        return f'{self.name} is eating {food}'

    def execute(self, *args, **kwargs):
        return self.eat(*args, **kwargs)



# print(Animal.name)
lion = Animal('Lion')
print(lion.name)
print(lion.eat('meat'))
print(lion.execute('apple'))