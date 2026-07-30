# Lambda function in Python
# The lambda function is like any other function in Python. However,
# they are anonymous functions that contain only one line. In other words,
# everything must be contained into a single expression.

# list2 = [3, 23, 34, 512, 12, 90, 32, 23, 535, 5, 75, 4574, 23, 5, 123]
# list3 = [3, 23, 34, 512, 12, 90, 32, 23, 535, 5, 75, 4574, 23, 5, 123]
# list2.sort()
# list3.sort(reverse=True)
# # sorted(list2) # it returns a shallow copy of the list.
# print(list2)
# print(list3)

# sort() alone won't work with big structures.
list1 = [
    {'name': 'John', 'last name': 'Watson'},
    {'name': 'Abraham', 'last name': 'Wilson'},
    {'name': 'Elicia', 'last name': 'Louise'},
    {'name': 'Michael', 'last name': 'Mando'},
    {'name': 'William', 'last name': 'Shakespeare'},
]

# def order(item):
#     return item['name']

# list1.sort(key=order)
def printList(lists):
    for item in lists:
        print(item)

list1.sort(key=lambda item: item['name']) # Using lambda
list2 = sorted(list1, key=lambda item: item['last name'])
printList(list2)