# Maintaining state within the class
class Camera:
    def __init__(self, name, filming=False):
        self.name = name
        self.filming = filming

    def film(self):
        if self.filming:
            print(f'{self.name} is already filming...')
            return

        print(f'{self.name} is filming...')
        self.filming = True # State

    def stop_film(self):
        if not self.filming:
            print(f'{self.name} is not filming...')
            return

        print(f'{self.name} is stopping filming...')
        self.filming = False

    def photograph(self):
        if self.filming:
            print(f'{self.name} cannot photograph while filming...')
            return

        print(f'{self.name} is photographing...')
        self.filming

c1 = Camera('Canon')
c2 = Camera('Sony')
c1.film()
c1.film()
c1.photograph()
c1.stop_film()
c1.photograph()
c1.stop_film()
print()
c2.photograph()
c2.film()
c2.stop_film()
c2.photograph()