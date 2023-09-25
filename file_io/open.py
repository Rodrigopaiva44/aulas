name = input("Whats your name? ")

# If we try to write more names, it will save only the last one.
file = open("names.txt", "w")  # change by "a" instead of "w"
file.write(name)
file.close()

# A better way to open a file: with
with open("names.txt", "a") as file:
    file.write(f"{name}\n")


# readind all the lines returning a list
with open("names.txt", "r") as file:  # We did not need to specify "r"
    lines = file.readlines()

for line in lines:
    print(line)

# An elegant way to do the same thing
with open("names.txt", "r") as file:
    for line in file:
        print("hello", line.rstrip())


# What if we want do sort the names before printing?
names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")
