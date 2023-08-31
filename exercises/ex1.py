class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        return f'Name: {self.name}\nAge: {self.age}'
    
    @classmethod
    def get(cls):
        name = input('')
        age = int(input(''))
        return cls(name,age)
    
persona1 = Person.get()
print(persona1.display_info())
