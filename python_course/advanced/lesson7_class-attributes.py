# Class attributes
class Person:
    current_year = 2026 # class attribute

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_birthyear(self):
        return Person.current_year - self.age # It's possible to access class attribute with self, but it's no recommended.

p1 = Person('John', 32)
p2 = Person('Louise', 25)
print(Person.current_year)
# Person.current_year = 1
print(p1.get_birthyear())
print(p2.get_birthyear())