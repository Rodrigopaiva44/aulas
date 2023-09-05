from random import randint
from time import sleep

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print(f'{self.model} is starting...')
        x = randint(1,6)
        sleep(x)
        return f'The {self.model} has already started'
    
    def __str__(self):
        return f"The {self.make}'s {self.model}, {self.year}"
    
car = Car('Honda', 'Civic', 2007)
print(car)
print(car.start_engine())