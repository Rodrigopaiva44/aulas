# Se o usuario nao consegue interagir o design ta mal feito

# SyntaxError são erros que não podemos lidar com
# precisamos voltar no código e resolver
# print("hello world!)

# ValueError
try:
    x = int(input("Whats x? "))  # cat
    print(f"x is {x}")
except ValueError:
    print("X is not an integer")

# NameError
try:
    x = int(input("Whats x? "))  # cat
except ValueError:
    print("X is not an integer")
print(f"x is {x}")

# Else
try:
    x = int(input("Whats x? "))  # cat
except ValueError:
    print("X is not an integer")
else:
    print(f"x is {x}")

# Reprompting, break
while True:
    try:
        x = int(input("Whats x? "))  # cat
    except ValueError:
        print("X is not an integer")
    else:
        break
print(f"x is {x}")

# def get_int


def main():
    x = get_int()  # get_int("Whats x? ")
    print(f"X is {x}")


def get_int():  # crie um parametro "msg"
    while True:
        try:
            x = int(input("Whats x? "))
            # return int(input("Whats x? ")) # "msg" here
        except ValueError:
            # pass
            print("X is not an integer")
        else:
            return x


main()
