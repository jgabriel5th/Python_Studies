class Cat:
    current_year = 2026
    def __init__(self, name, age, genre, breed, eating=False):
        self.name = name
        self.age = age
        self.genre = genre
        self.breed = breed
        self.eating = eating

    def eat(self):
        if self.eating:
            print(f'{self.name} is already eating...')
            return

        print(f'{self.name} is eating...')
        self.eating = True

    def stop_eating(self):
        if not self.eating:
            print(f'{self.name} is not eating...')
            return

        print(f'{self.name} is stopping eating...')
        self.eating = False

    def meow(self):
        if self.eating:
            print(f'{self.name} cannot meow while eating...')
            return

        print(f'{self.name} is meowing...')

    def get_birthyear(self):
        print(f'{Cat.current_year - self.age}')

cat1 = Cat('Newton', 8, 'Male', 'Tiger')
cat2 = Cat('Oliver', 2, 'Male', 'Artic Tiger')
cat1.meow()
cat1.eat()
cat1.eat()
cat1.meow()
cat1.stop_eating()
cat1.stop_eating()
cat1.meow()
cat1.get_birthyear()