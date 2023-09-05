def main():
    print(f"The SQUARE of 2 is {square(2)}")


def square(x):
    return x*x


# by not using the condition __name__ == "__main__", whenever we import this
# file the main function will execute.
if __name__ == "__main__":
    main()
