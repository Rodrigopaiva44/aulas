class Book:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    def __str__(self):
        return f'Name: {self.name}\nAuthor: {self.author}\nYear: {self.year}'

    def age(self):
        age = 2023 - self.year
        return age


   
book1 = Book('Reinações de Narizinho', 'Monteiro Lobato', 1931)
print(book1)
print(f'Age: {book1.age()}')