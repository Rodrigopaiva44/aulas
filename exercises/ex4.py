class Estudent:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def add_grade(self):
        for i in range(1,5):
            note = float(input(f"Enter the {i}th student's grade: "))
            self.grade.append(note)
        return self.grade

    def media_grades(self):
        media = sum(self.grade) / len(self.grade)
        return media

    def __str__(self):
        return f'Name: {self.name}\nAge: {self.age}\nGrade: {self.grade}'


name = input("Enter the estudent's name: ")
age = input("Enter the estudent's age: ")
notes = []
estudent = Estudent(name,age,notes)
print(estudent.add_grade())
print(estudent.media_grades())

print(estudent)

# media = sum(minha_lista) / len(minha_lista)