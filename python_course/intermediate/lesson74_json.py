import json

# person = {
#     'name': 'John',
#     'lastname': 'Watson',
#     'Addresses': [
#         {'street': 'R1', 'number': 33},
#         {'street': 'R2', 'number': 56},
#     ],
#     'height': 1.9,
#     'favorite_numbers': (2, 4, 6, 8, 10),
#     'dev': True,
#     'none': None
# }

file_path = 'lesson74_json.json'
# with open(file_path, 'w') as file:
#     json.dump(person, file, indent=2, ensure_ascii=False)

with open(file_path, 'r') as file:
    person = json.load(file)
    print(person)
    print(person['name'])