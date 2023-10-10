def main():
    n = int(input("Whats n: "))

    for i in range(n):
        print(bee(i))


def bee(n):
    return "zZz"*n

# What if we make this code better?


def main2():
    n = int(input("Whats n: "))

    for i in bee2(n):
        print(bee(i))


def bee2(n):
    swarm = []
    for i in range(n):
        swarm.append("ZzZ"*i)
    return swarm


def main3():
    n = int(input("Whats n: "))

    for i in bee3(n):
        print(i)


def bee3(n):
    for i in range(n):
        yield "ZzZ"*i


if __name__ == "__main__":
    main3()
