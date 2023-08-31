class Student:
    def __init__(self, name, home, age):
        if not name:
            # raise TestError("We can create a new error class")
            raise ValueError("No name was given")
        if home not in ["Vila isabel", "Rio de janeiro", "Rio"]:
            raise ValueError("Invalid home")
        self.name = name
        self.home = home
        self.age = age

    # Special method that returns a string when we pass our object in functions
    def __str__(self):
        return f"{self.name} from {self.home}"

    def speak(self):
        match self.age:
            case 20:
                return "bó lapa"
            case 18:
                return "bó lol"
            case 16:
                return "vou nada"
            case _:
                return "Não estudo no CB"


def main():
    student = get_student()
    print(student)  # will show where in the computer's memory it is
    print(student.speak())


def get_student():
    name = input("Name: ")
    home = input("Home: ")
    age = int(input("Age: "))
    try:
        return Student(name, home, age)
    except ValueError:
        print("Error!!!")


if __name__ == "__main__":
    main()
