import json
import os
# people = [
#     {
#         "name": "mary",
#         "lastname": "jackson",
#         "age": 32,
#         "status": False,
#         "grades": ['A', 'A+'],
#         "phones": {
#             "residential": "00 0000-0000",
#             "cellphone": "00 0000-0000",
#         }
#     },
#     {
#         "name": "tom",
#         "lastname": "riddle",
#         "age": 48,
#         "status": True,
#         "grades": ['B', 'A'],
#         "phones": {
#             "residential": "00 0000-0000",
#             "cellphone": "00 0000-0000",
#         }
#     }
# ]


# BASE_DIR = os.path.dirname(__file__)
# SAVE_TO = os.path.join(BASE_DIR, 'python-file.json')

# with open(SAVE_TO, 'w') as file:
#     json.dump(people, file, indent=2) # people(dictionary), file, indent=2(to format the file).

BASE_DIR = os.path.dirname(__file__)
JSON_FILE = os.path.join(BASE_DIR, 'python-file.json')

with open(JSON_FILE, 'r') as file:
    people = json.load(file) # Used to load a json file.
    print(people)
