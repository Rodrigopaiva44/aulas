
def power(x, n): return x ** n


result = power(2, 3)
print(result)

words = ["apple", "banana", "cherry", "date"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)


def celsius_to_fahrenheit(celsius): return (celsius * 9/5) + 32


temperature_celsius = 25
temperature_fahrenheit = celsius_to_fahrenheit(temperature_celsius)
print(f"{temperature_celsius}°C é igual a {temperature_fahrenheit}°F")


def is_even(x): return x % 2 == 0


number = 7
if is_even(number):
    print(f"{number} é um número par.")
else:
    print(f"{number} é um número ímpar.")
