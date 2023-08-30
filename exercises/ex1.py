class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        return f'Name: {self.name}\nAge: {self.age}'
    
persona1 = Person('Vitor', 19)
print(persona1.display_info())
