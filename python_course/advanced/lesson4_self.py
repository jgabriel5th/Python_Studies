# Understanding self in Python classes
# By conviction, self is used to reference the instance.
# Class - Mold(usually without data)
# Class instance(object) - Has data
# A class can generate several instances.
# In the class, self is the instance itself.
class Car:
    def __init__(self, name):
        self.name = name

    def accelerate(self):
        return f'{self.name} is accelerating...'

fusca = Car('Fusca')
print(fusca.name)
print(fusca.accelerate())
print(Car.accelerate(fusca))


celta = Car(name='Celta')
print(celta.name)
print(celta.accelerate())
print(Car.accelerate(celta))