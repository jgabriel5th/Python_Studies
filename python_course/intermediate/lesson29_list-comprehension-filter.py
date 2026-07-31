# Introduction to List comprehension in Python
# List comprehension is a faster way to create lists
# from iterables.
# print(list(range(10)))
import pprint

def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)


list1 = []
for number in range(10):
    list1.append(number)
# print(list1)

list1 = [number * 2 for number in range(10)]
# print(list1)

# # Mapping the data in list comprehension
products = [
    {'name': 'p1', 'price': 20, },
    {'name': 'p2', 'price': 10, },
    {'name': 'p3', 'price': 30, },
]
# new_products = [{'name': product['name'], 'price': product['price']} for product in products]
new_products = [{**product, 'price': product['price'] * 1.05} if product['price'] > 20 else {**product} for product in products]

# print(new_products)
# p(new_products)

# Filter - if that comes after for in list comprehension.
list2 = [n for n in range(10) if n < 5] # else is not included in filter.
# print(list2) # Output: [0, 1, 2, 3, 4]
new_products = [
    {**product, 'price': product['price'] * 1.05} # Mapping comes before for
    if product['price'] > 20 else {**product} 
    for product in products 
    if product['price'] > 10] # Filtering comes after for
# p(new_products)

# Practing:
books = [
    {'book': 'Harry Potter and the Goblet of Fire', 'amount': 8, },
    {'book': 'Sherlock Holmes', 'amount': 4, },
    {'book': 'Percy Jackson and the Olympians', 'amount': 5, },
    {'book': 'Bible', 'amount': 5, },
]
available_books = [{'book': data['book'], 'amount': data['amount'] - 5 if data['book'] == 'Bible' else data['amount']} for data in books]
print(*available_books, sep='\n')