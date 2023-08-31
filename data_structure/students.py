students = ["Vitin", "Rodrigo", "Renan"]

# Iterating over the objects inside the list
for student in students:
    print(student)

for s in range(len(students)):
    print(s, students[s])

# What if we need to associate the student name with something else?
# With lists it would be like
# students= ["Vitin",...]
# houses = ["cabuçu",...]

students = {
    "Vitin": "Cabuçu",
    "Rodrigo": "Vila Isabel",
    "Renan": "Pavuna"
}

for student in students:  # iterating over the keys
    print(student, students[student])

students = [
    {"name": "Vitin", "home": "Cabuçu"},
    {"name": "Rodrigo", "home": "Vila Isabel"},
    {"name": "Renan", "home": "Pavuna"}
]

for student in students:
    print(student["name"], student["home"], sep=", ")
