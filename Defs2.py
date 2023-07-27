def factorial(n):
    f = 1
    for c in range(1, n+1):
        f *= c
    return f


n = int(input('Digit a number: '))
fat = factorial(n)
print(f'The factorial of {n} is {fat}')