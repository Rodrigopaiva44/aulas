# Lets format a name from user input

import re

# Without REGEX

name = input("Name: ").strip()
# if "," in name:
#     last, first = name.split(", ")  # name.split(", ?") REGEX
#     name = f"{first} {last}"
# print(f"hello, {name}")

# Note that in this example the input is coming from the keyboard, from you.
# At csv file for example, we dont have that situation.

matches = re.search(r"^(.+), (.+)$", name)
if matches:
    last, first = matches.groups()  # returns anything that is in () ex: (.+)
    name = f"{first} {last}"
print(f"hello, {name}")

# Another way
if matches:
    last = matches.group(1)
    first = matches.group(2)
    name = f"{first} {last}"
print(f"hello, {name}")

# Why using unnecessary variables?
if matches:
    # why the first group is 1 and not 0? Just a convention.
    name = matches.group(1) + " " + matches.group(2)
print(f"hello, {name}")  # hello, Paiva,Rodrigo


matches = re.search(r"^(.+), ?(.+)$", name)  # add a question mark
if matches:
    last, first = matches.groups()
    name = f"{first} {last}"
print(f"hello, {name}")  # hello, Rodrigo Paiva


# but if we have a lot of spaces ex: Paiva,      Rodrigo
matches = re.search(r"^(.+), *(.+)$", name)  # add a star
if matches:
    last, first = matches.groups()
    name = f"{first} {last}"
print(f"hello, {name}")  # hello, Rodrigo Paiva

# A new syntax for Python :D
if matches := re.search(r"^(.+), *(.+)$", name):  # := (walrus operator)
    last, first = matches.groups()
    name = f"{first} {last}"
print(f"hello, {name}")
# we can do both things:
# Create a variable called "matches" that contains re.search() return
# And verifying the if conditional: if True/False:
