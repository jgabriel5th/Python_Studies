# Issues in mutable parameters in Python functions.
def add_clients(name, lista=[]):
    lista.append(name)
    return lista

client1 = add_clients('John')
add_clients('Louise', client1)
print(client1)

client2 = add_clients('Elícia')
add_clients('Abraham', client2) # Everytime list is not specified, Python will reuse the mutable parameter in both variables.
print(client2)

# A way to fix: creating a list and using it as parameter
list1 = []
list2 = []
client3 = add_clients('John', list1)
add_clients('Louise', client3)
print(client3)

client4 = add_clients('Elícia', list2)
add_clients('Abraham', client4) # Everytime list is not specified, Python will reuse the mutable parameter in both variables.
print(client4)

# The best way to fix it: not using mutable parameter in a function
def add_clientsFixed(name, lista=None):
    if lista is None:
        lista = []
    lista.append(name)
    return lista

client5 = add_clientsFixed('Rocky')
add_clientsFixed('Balboa', client5)
add_clientsFixed('Rambo', client5)
client5.append('Someone')
print(client5)

client6 = add_clientsFixed('Chester')
add_clientsFixed('Bennington', client6)
print(client6)