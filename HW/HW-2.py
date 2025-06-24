
class Heroes:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def action(self):
        print(f"{self.name} says:'Hello!'")

class Archer(Heroes):
    def __init__(self,name, hp, arrows, precision):
        super().__init__(name, hp)
        self.arrows = arrows
        self.precision = precision
    def attack(self):
        print(f'{self.name} attack!')
        self.arrows -= 1
        if self.precision >= 1:
            print(f'{self.name} hit!')
        else:
            print(f'{self.name} miss!')
    def rest(self):
        print(f'{self.name} rested nicely!')
        self.arrows += 3
    def status(self):
        print(f'Имя:{self.name}.Здоровье:{self.hp}.Стрелы:{self.arrows}.Точность:{self.precision}')

Elzie = Archer('Elzie', 100, 5, 1)
Elzie.action()
Elzie.status()
Elzie.attack()