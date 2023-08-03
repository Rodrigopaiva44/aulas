# a simple way, not incorrect but inconsistent
name = input("Name: ")
home = input("Home: ")
print(f"{name} from {home}")


# Using main
def main_1():
    name = get_name()
    home = get_home()
    print(f"{name} from {home}")


def get_name():
    return input("Name: ")  # why use variables?


def get_home():
    return input("Home: ")


# Working smart with tuples
def main_2():
    student = get_student_2()  # unpacking
    print(f"{student[0]} from {student[1]}")


def get_student_2():
    name = input("Name: ")
    home = input("Home: ")
    return (name, home)  # returning a value with 2 values (tuple)


# How to overwrite an error using list
def main_3():
    student = get_student_3()
    if student[0] == "Rodrigo":  # using list we can overwrite
        student[1] = "Vila Isabel"
    print(f"{student[0]} froms {student[1]}")


def get_student_3():
    name = input("Name: ")
    home = input("Home: ")
    return [name, home]  # use [] to return a mutable list


# Using dicts to be more clean
def main_4():
    student = get_student_4()
    if student["name"] == "Rodrigo":
        student["home"] = "Vila Isabel"
    # Be sure to use single quotes
    print(f"{student['name']} froms {student['home']}")


def get_student_4():
    student = {}
    student["name"] = input("Name: ")
    student["Home"] = input("Home: ")
    return student

# Why use unnecessary variables


def get_student_5():
    name = input("Name: ")
    home = input("Home: ")
    return {"name": name, "home": home}

# Creating a class


class Student:
    ...


def main():
    student = get_student()
    print(f"{student.name} froms {student.home}")


def get_student():
    student = Student()
    # Classes have attributes
    student.name = input("Name: ")
    student.home = input("House: ")
    return student


if __name__ == "__main__":
    main()
