
from time import sleep

senha = ''
n = str(input('Qual seu nome?\nR: ')).strip().upper()

if n in 'MESTRE':
    senha = input('Qual a senha?\nR:')
    if senha in 'bala':
        r = int(input("Olá, Mestre. O que deseja?\n"
                      "[0] DESLIGAR O SISTEMA\n"
                      "[1] TABUADA\n"
                      "[2] CALCULADORA\n"
                      "R:"))
        if r == 0:
            print('Desligando...')
            print('OFF')
        if r == 1:
            print('TABUADA ROPRO')
            nt = int(input('Digite um número que queira ver a tabuada: '))
            print('CALCULANDO...')
            sleep(0.5)
            for c in range(1, 10):
                print(f'{nt} x {c} = {nt * c}')
            sleep(0.1)
        if r == 2:
            print('CALCULADORA ROPRO')
            nc = float(input('Digite o primeiro número: '))
            s = str(input('Digite o sinal: '))
            nc2 = float(input('Digite o segundo número: '))
            if s in '+':
                print(f'{nc + nc2}')
            if s in '-':
                print(f'{nc - nc2}')
            if s in '*':
                print(f'{nc * nc2}')
            if s in '/':
                print(f'{nc / nc2}')
    else:
        print('\033[31mSENHA ERRADA!')
else:
    print(f'Olá, {n}!')
