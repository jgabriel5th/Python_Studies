list1 = []
for x in range(3):
    for y in range(3):
        list1.append((x, y))

list1 = [(x, y) for x in range(3) for y in range(3)] # List comprehension
print(list1)