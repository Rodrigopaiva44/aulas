try:
    a = int(input('Firts Number: '))
    b = int(input('Second one: '))
    r = a / b
except (ValueError, TypeError):
    print('We had a problem with the data types that you digit')
except ZeroDivisionError:
    print('Division by Zero is not possible')
except KeyboardInterrupt:
    print('Data not informed')
except Exception as error:
    print(f'The error was {error.__cause__}')
else:
    print(f'The result is {r:.1f}')
finally:
    print('Come back always')
