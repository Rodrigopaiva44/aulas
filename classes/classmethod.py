class Student:
    def __init__(self, name, home):
        if not name:
            raise ValueError("No name was given")
        self.name = name
        self.home = home

    def __str__(self):
        return f"{self.name} from {self.home}"

    @classmethod
    def get(cls):
        name = input("Name: ")
        home = input("Home: ")
        return cls(name, home)


def main():
    student = Student.get()
    print(student)


if __name__ == "__main__":
    main()
