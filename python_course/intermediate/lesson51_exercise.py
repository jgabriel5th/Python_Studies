from copy import deepcopy
# Exercises
# Increase the prices of the following products by 10%.
# Generate new_products by deep copy.
products = [
    {'name': 'Product 5', 'price': 10.00},
    {'name': 'Product 1', 'price': 22.32},
    {'name': 'Product 3', 'price': 10.11},
    {'name': 'Product 2', 'price': 105.87},
    {'name': 'Product 4', 'price': 69.90},
]
new_products = [{**product, 'price': round(product['price'] * 1.10, 2)} for product in deepcopy(products)]
print('NEW PRODUCTS(10% INCREASE):')
print(*new_products, sep='\n')

# Order the products by name (descending)
# Generate products_ordered_by_name by deep copy
products_ordered_by_name = deepcopy(products)
products_ordered_by_name = sorted(products_ordered_by_name, key=lambda product: product['name'], reverse=True)
print('PRODUCTS ORDERED BY NAME(DESCENDING):')
print(*products_ordered_by_name, sep='\n')

# Order the products by name (ascending)
# Generate products_ordered_by_price by deep copy
products_ordered_by_price = deepcopy(products)
products_ordered_by_price = sorted(products_ordered_by_price, key=lambda product: product['price'])
print('PRODUCTS ORDERED BY PRICE(ASCENDING):')
print(*products_ordered_by_price, sep='\n')