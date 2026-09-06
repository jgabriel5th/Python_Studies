# class - Classes are molds to create new objects
# The classes generate new objects(instances) that
# can have their own attributes and methods.
# The generated objects by the class can use its inner data
# to do several actions.
# By convention, it's used PascalCase to classes name.
# string = 'John' # str
# print(string.upper())
# print(isinstance(string, str))
class Person:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname



p1 = Person('John', 'Watson')
# p1.name = 'John'
# p1.lastname = 'Watson'

p2 = Person('Abraham', 'Gabriel')
# p2.name = 'Abraham'
# p2.lastname = 'Gabriel'

print(p1.name)
print(p1.lastname)

print(p2.name)
print(p2.lastname)