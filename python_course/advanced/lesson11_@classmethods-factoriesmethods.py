# Class methods + factories
# These are methods in which "self" will be "cls", which means,
# instead receiving the instance in the first parameter, it'll
# be received the class itself.
class Person:
    current_year = 2026 # class attribute

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod # With this decorator, the method below will be a class method
    def class_method(cls): # It's crucial put cls as parameter.
        print('Hey')

    @classmethod 
    def create_with_50_years(cls, name):
        return cls(name, 50) # factory method

    @classmethod
    def create_without_name(cls, age):
        return cls('Unknown', age)

print(Person.current_year)
p1 = Person('Abraham', 37)
Person.class_method()
p2 = Person.create_with_50_years('James')
print(p2.name, p2.age)
p3 = Person.create_without_name(43)
print(p3.name, p3.age)