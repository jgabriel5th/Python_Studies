# Exercise - Save your class in JSON
# Save the data of your class in JSON
# and then create again the instances
# of the class with the saved data
# Make it in separated files.
import json
FILE_PATH = 'lesson9a.json'
class Person:
    def __init__(self, name, age, genre):
        self.name = name
        self.age = age
        self.genre = genre



p1 = Person('John', 25, 'Man')
p2 = Person('Mary', 33, 'Woman')
p3 = Person('Abraham', 38, 'Man')
bd = [vars(p1), vars(p2), vars(p3)]

def make_dump():
    with open(FILE_PATH, 'w') as file:
        print('Making dump')
        json.dump(bd, file, indent=2, ensure_ascii=False)   

if __name__ == '__main__':
    print('This is the __main__')
    make_dump()