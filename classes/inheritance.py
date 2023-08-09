class _Student:
    def __init__(self, name, home):
        if not name:
            raise ValueError("Missing name")
        self.name = name
        self.home = home


class _Professor:
    def _init__(self, name, subject):
        # RED FLAG:
        # When we start copy and paste things probably there's a better way
        if not name:
            raise ValueError("Missing name")
        self.name = name
        self.subject = subject


# To solve this we can use inheritance

class Person:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name

    ...


class Student(Person):
    def __init__(self, name, home):
        super().__init__(name)  # Reference to a super/parent class (Person)
        self.home = home
    ...


class Professor(Person):
    def _init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
    ...


person = Person("Antonio")
student = Student("Vitin", "Cabuçu")
professor = Professor("Rodrigo", "Python")
