import json
from lesson9_exercise import FILE_PATH, Person, make_dump

# make_dump()
with open(FILE_PATH, 'r') as file:
    people = json.load(file)
    p1 = Person(**people[0])
    p2 = Person(**people[1])
    p3 = Person(**people[2])

    print(p1.name, p1.age, p1.genre)
    print(p2.name, p2.age, p2.genre)
    print(p3.name, p3.age, p3.genre)

print(__name__)