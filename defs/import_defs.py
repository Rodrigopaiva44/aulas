from use_case_defs import dobra


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
if par(num):
    print('é par')
else:
    print('Não é par')


print(dobra([1, 2, 3]))
