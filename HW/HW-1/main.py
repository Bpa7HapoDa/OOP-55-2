class person:
    def __init__(self, name='noname', age=1, city='none'):
        self.name = name
        self.age = age
        self.city = city
    def introduce(self):
        return f'Привет, меня зовут {self.name}, мне {self.age}, мой город {self.city}'
    def is_adult(self):
        if self.age >= 18:
            return True
        else:
            return False



atai = person('Atai', 19, 'Bishkek')
ayana = person('Ayana', 17, 'Moscow')
kairat = person('Kairat',18, 'Almaty')
print(atai.introduce())
print(atai.is_adult())
print(ayana.is_adult())
