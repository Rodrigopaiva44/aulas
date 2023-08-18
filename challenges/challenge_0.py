# Determine se um número é par ou impar sem usar condições

n = int(input("n: "))
print("Par" * (n % 2 == 0), "Impar" * (n % 2 != 0))
