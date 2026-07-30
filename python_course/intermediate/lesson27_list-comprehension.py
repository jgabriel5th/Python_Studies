# List comprehension in Python
# List comprehension is a faster way to create lists
# from iterables.
# print(list(range(10)))

# Ordinary way to fill list1:
list1 = []
for number in range(10):
    list1.append(number)
# print(list1)

# List comprehension way:
list1 = [number for number in range(10)] # operation has to be before for
list2 = [number * 2 for number in range(10)]
print(list1)
print(list2)
