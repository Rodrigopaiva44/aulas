# A cat that meows 3 times
print("Meow")
print("Meow")
print("Meow")

# What if that cat meows 50 times?
# Are you gonna copy and paste 50 times too?
# Thats why loops

i = 3
while i != 0:
    print("meow")
    # If we not change i, this is gonna end up in a infinite loop
    i = i - 1
# We can do the opposite and sum i to 3
i = 1
while i <= 3:
    print("meow")
    i = i + 1

# Foor loop
for i in [0, 1, 2]:
    print("meow")
# What if i need to loop 1 milion times?
for _ in range(1000000):  # Notice that we don't use the variable created (i)
    print("meow")

# What's the main difference?

# At the end if we just want to print meow use int
print("meow" * 3)
