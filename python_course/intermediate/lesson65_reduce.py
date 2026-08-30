from functools import reduce
# reduce - make a reduction of an iterable in a value
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

# def reduce_function(accumulator, product):
#     print('accumulator', accumulator)
#     print('product', product)
#     print()
#     return accumulator + product['price']

total = reduce(
    # reduce_function
    lambda ac, p: ac + p['price'], products, 0
)

print('Total:', round(total, 2))

# total = 0
# for price in products:
#     total += price['price']
# print(round(total, 2))

# total = sum([p['price'] for p in products]) # list comprehension
# print(round(total, 2))