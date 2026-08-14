# Yield from
def gen1():
    yield 1
    yield 2
    yield 3

def gen2(gen=None):
    if gen is not None:
        yield from gen # The function execution will be delayed¹
    yield 4
    yield 5
    yield 6

def gen3(gen):
    yield from gen() # Function being executed here.
    yield 7
    yield 8
    yield 9

g1 = gen3(gen2)
g2 = gen3(gen1)
g3 = gen2(gen1()) # Function being executed here²
for n in g1:
    print(n)
print('OVER')

for n in g2:
    print(n)
print('OVER')

for n in g3:
    print(n)
print('OVER')