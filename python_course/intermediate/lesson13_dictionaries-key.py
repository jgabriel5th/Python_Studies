# Manipulating keys and values in dictionaries
person = {}

person['name'] = 'Isaac' # New key with its value created in the dictionary.
person['last name'] = 'Nilton'
person['last name'] = 'Newton' # Editing
person['age'] = 49
print(person)
del person['age'] # Deleting a key
print(person)
# print(person['name1']) # KeyError

# Dynamically:
person1 = {}
key = 'full_name'
person1[key] = 'Isaac Newton'
print(person1[key])

# get():
# if doesn't work when an exception is raised, an option to overcome this is to use get().
if person.get('age') is None:
    print('It does not exist')
else:
    print(person['age'])

print('This code will be executed')