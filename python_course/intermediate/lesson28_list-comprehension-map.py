# Introduction to List comprehension in Python
# List comprehension is a faster way to create lists
# from iterables.
# print(list(range(10)))
list1 = []
for number in range(10):
    list1.append(number)
# print(list1)

list1 = [number * 2 for number in range(10)]
print(list1)

# # Mapping the data in list comprehension
products = [
    {'name': 'p1', 'price': 20, },
    {'name': 'p2', 'price': 10, },
    {'name': 'p3', 'price': 30, },
]
# new_products = [{'name': product['name'], 'price': product['price']} for product in products]
new_products = [{**product, 'price': product['price'] * 1.05} if product['price'] > 20 else {**product} for product in products]

# print(new_products)
print(*new_products, sep='\n')

# Practing
tasks = [
    {'task': 'code', 'how long': 2, },
    {'task': 'play games', 'how long': 1, },
    {'task': 'study', 'how long': 3, },
]
new_tasks = [{**task, 'how long': task['how long'] * 1.50} if task['how long'] < 2 else {**task} for task in tasks]
print(*new_tasks, sep='\n')