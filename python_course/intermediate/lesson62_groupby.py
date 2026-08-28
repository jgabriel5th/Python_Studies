# groupby - grouping values (itertools)
from itertools import groupby

students = [
    {'name': 'Andrew', 'grade': 'A'},
    {'name': 'Abraham', 'grade': 'A'},
    {'name': 'Jacob', 'grade': 'B'},
    {'name': 'Joseph', 'grade': 'A'},
    {'name': 'Isaac', 'grade': 'B'},
    {'name': 'John', 'grade': 'B'},
    {'name': 'Anderson', 'grade': 'C'},
    {'name': 'Mary', 'grade': 'A'},
    {'name': 'Louise', 'grade': 'A'},
]

def order(student):
    return student['grade']

grouped_students = sorted(students, key=order)


# students = ['a', 'a', 'a', 'a', 'b', 'c', 'a']
# groups = groupby(sorted(students)) # If sorted() is not used, then it'll create another group 'a', since it's not ordered.

groups = groupby(grouped_students, key=order)

for group, grouper in groups:
    print(group)
    for students in grouper:
        print(students)