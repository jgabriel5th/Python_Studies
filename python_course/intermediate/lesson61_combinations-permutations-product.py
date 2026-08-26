# Combinations, Permutations and Product - Itertools
# Combination - Order does not matter - iterable + group size
# Permutation - Order matters
# Product - Order matters and repeat unique values.
from itertools import combinations, permutations, product

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

people = [
    'João', 'Joana', 'Luiz', 'Letícia',
]
tshirts = [
    ['black', 'white'],
    ['p', 'm', 'g'],
    ['masculine', 'feminine', 'unisex'],
    ['cottom', 'polyester']
]

print('COMBINATIONS:')
print_iter(combinations(people, 2))
print('PERMUTATIONS:')
print_iter(permutations(people, 2))
print('PRODUCTS:')
print_iter(product(*tshirts))