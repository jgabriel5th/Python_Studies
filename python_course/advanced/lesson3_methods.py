# Methods in instances from Python classes
# Hard coded - something that was written directly in the code.
class Car:
    def __init__(self, name):
        self.name = name

    def accelerate(self):
        return f'{self.name} is accelerating...'

fusca = Car('Fusca')
print(fusca.name)
print(fusca.accelerate())


celta = Car(name='Celta')
print(celta.name)
print(celta.accelerate())
