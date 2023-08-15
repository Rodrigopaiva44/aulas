# Define a function
def __hello():
    print("hello")


name = input("Whats your name? ")
__hello()
print(name)


# Creating our own parameters
def _hello(n):
    print("hello", n)


name = input("Whats your name? ")
_hello(name)


# optional parameter
def hello(n="World"):
    print("hello", n)


name = input("Whats your name? ")
hello(name)

# Why use main?


def main():
    name = input("Whats your name? ")
    hello(name)


def hello(n="World"):
    print("hello", n)


main()


# returning values

def main():
    x = int(input("Whats x: "))
    print("x squared is", square(x))


def square(num):
    return num * num


main()
