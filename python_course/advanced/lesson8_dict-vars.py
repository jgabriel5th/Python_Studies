# __dict__ and vars for instance attributes
class Person:
    current_year = 2026

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_birthyear(self):
        return Person.current_year - self.age

data = {'name': 'John', 'age': 38}
p1 = Person(**data)
# p1.name = 'WHOA'
# print(p1.age)
# p1.__dict__['other'] = 'thing' # Normally not used
# p1.__dict__['name'] = 'WHOA'
# # del p1.__dict__['name']
# print(p1.__dict__)
print(vars(p1))