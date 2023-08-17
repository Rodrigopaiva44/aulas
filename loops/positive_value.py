# How to get a positive number by input
while True:
    n = int(input("What's n: "))
    if n < 0:
        continue  # Continue the loop
    else:
        break  # get out of the loop

while True:
    n = int(input("What's n: "))
    if n > 0:
        break


for _ in range(n):
    print("meow")

# Create a meow function


def main():
    number = get_number()
    meow(number)


def get_number():
    while True:
        n = int(input("What's n: "))
        if n > 0:
            return n


def meow(n):
    for _ in range(n):
        print("meow")
