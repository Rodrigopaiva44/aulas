with open("students.csv") as file:
    for line in file:
        row = line.rstrip().split(",")  # row = linha
        print(f"{row[0]} is from {row[1]}")


# A better way
students = []

with open("students.csv") as file:
    for line in file:
        name, home = line.rstrip().split(",")
        students.append(f"{name} is from {home}")

for student in sorted(students):
    print(student)


students = []

with open("students.csv") as file:
    for line in file:
        name, home = line.rstrip().split(",")
        student = {"name": name, "home": home}
        students.append(student)


def get_name(student):
    return student["name"]


for student in sorted(students, key=get_name):
    print(f"{student['name']} is from {student['home']}")

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")
