class Employe:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self) -> str:
        return f'{self.name}\n{self.position}\n${self.salary}'
    

    def apply_raise(self):
        percent = float(input('Enter the value of inscrease on percents: %'))
        result = (percent / 100) * self.salary
        self.salary += result
        return f'${self.salary}'

employe = Employe('Michael Scott', 'Regional Mananger', 3500)
print(employe)
print('Applying...')
print(employe.apply_raise())

"""
porcentagem = 5
total = 25
valor = (porcentagem / 100) * total
print(valor)

"""