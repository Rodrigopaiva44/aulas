import re

email = input("Whats your email?").strip()

# re.search(pattern,string,flags=0)

if re.search("@", email):
    print("Valid")
else:
    print("Invalid")

# a pattern could be read like a re, "@" its a re but a weak one
# .  any character except a newline
# *  0 or more repetitions (repetitions = characther)
# +  1 or more repetitions
# ?  0 or 1 repetitions
# {m}  m repetitions
# {m,n}  m-n repetitions

if re.search(".*@.*", email):  # change "*" to "+" bc "*" accepts any char
    print("Valid")
else:
    print("Invalid")

# how can we express literally "." ?
if re.search(r".+@.+\.com", email):  # use "\" escape sequence and r"" (raw)
    print("Valid")
else:
    print("Invalid")

# Try: My email is rodrigopaiva@gmai.com

# ^ matches the start of the string
# $ matches the end of the string or just before the newline
# at the end of the string

if re.search(r"^@.+\.com$", email):
    print("Valid")
else:
    print("Invalid")

# [] sets of characters ex: [abcdefg] [a-zA-Z0-9]
# [^] complementing the set ex: [^@] means anything but the "@"

if re.search(r"^[^@]+@[^@]+\.com$", email):
    print("Valid")
else:
    print("Invalid")


if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.com$", email):
    print("Valid")
else:
    print("Invalid")

# \w means world character (alpha, numeric, symble or underscore)
if re.search(r"^\w+@\w+\.com$", email):
    print("Valid")
else:
    print("Invalid")

# we can add more domains at the and by using (|)
if re.search(r"^\w+@\w+\.(com|edu|gov|net)$", email,):
    print("Valid")
else:
    print("Invalid")

# What if we use uppercase?

# to resolve that use  re.IGNORECASE as a flag
if re.search(r"^\w+@\w+\.(com|edu|gov|net)$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")


if re.search(r"^.+is.+$", email):
    print("valid")
else:
    print("não")
