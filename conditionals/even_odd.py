def main():
    x = int(input("Whats x: "))
    if is_even(x):
        print("Even")  # Par
    else:
        print("Odd")  # Impar

# Boolean values


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


main()

# A Pythonic way of doing things


def is_even_pythonic(n):
    return True if n % 2 == 0 else False

# The most elegant way


def is_even_elegant(n):
    return n % 2 == 0

# Its up to you decide which way is better. If/Else could be more readable
