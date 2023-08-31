class Student:
    def __init__(self, name, home):
        if not name:
            raise ValueError("No name was given")
        self.name = name
        self.home = home

    def __str__(self):
        return f"{self.name} from {self.home}"

    # Getter function
    @property
    def home(self):
        return self._home

    # Setter function
    @home.setter
    def home(self, home):
        if home not in ["Vila isabel", "Rio de Janeiro", "Rio"]:
            raise ValueError("Invalid home")
        # We cant have methods and attributes with thesame name so we use _
        self._home = home


def main():
    student = get_student()
    # What if we try to overwrite the attribute we checked in init ?
    student.home = "Cabuçu"
    print(student)


def get_student():
    name = input("Name: ")
    home = input("Home: ")
    try:
        return Student(name, home)
    except ValueError:
        print("Error!!!")


if __name__ == "__main__":
    main()
