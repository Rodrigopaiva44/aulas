x = int(input("Whats X: "))
y = int(input("Whats Y: "))

# ask a question which return a boolean value (True or False)
if x < y:
    print("x is less than y")
if x > y:
    print("x is greater than y")
if x == y:
    print("x is equal to y")

# Using elif let us finish the code early if is the case
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
elif x == y:
    print("x is equal to y")

# We dont need to use elif on last question
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")

# operator OR

if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")

# Why asking two questions if we can just check if x is not equal to y (!=)
if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")

# Its up to you decide which logic use
if x == y:
    print("x is equal to y")
else:
    print("x is not equal to y")
