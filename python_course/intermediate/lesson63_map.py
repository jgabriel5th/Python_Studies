from functools import partial
from types import GeneratorType
# map - to map data
def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

products = [
    {'name': 'Product 5', 'price': 10.00},
    {'name': 'Product 1', 'price': 22.32},
    {'name': 'Product 3', 'price': 10.11},
    {'name': 'Product 2', 'price': 105.87},
    {'name': 'Product 4', 'price': 69.90},
]

# def increase_percentage(percentage): # Usually a closure would be made to create ways to make new functions.
#     def take_value(value):
#         return round(value * percentage, 2)
#     return take_value
# increase_ten_percent = increase_percentage(1.1)
def increase_percentage(value, percentage):
    return round(value * percentage, 2)
increase_ten_percent = partial(increase_percentage, percentage=1.1) # But will partial from functools, it's possible to create it.

# new_products = [
#     {**p, 'price': increase_ten_percent(p['price'])} for p in products
# ]

def changeProductPrice(product):
    return {**product, 'price': increase_ten_percent(product['price'])}

new_products = map(changeProductPrice, products)
print_iter(new_products)
print(hasattr(new_products,'__iter__'))
print(hasattr(new_products,'__next__')) # It's an iterator
print(isinstance(new_products, GeneratorType)) # But not a generator

print(
    list(map( # If not list is not put, it'll print a map object(because it's an iterator)
        lambda x: x * 3,
        [1, 2, 3, 4]
    )
))