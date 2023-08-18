# Crie um jogo par ou impar


import random

computador = random.randint(1, 10)
par_impar = ""
soma = pontos_usuario = pontos_computador = 0

while True:
    par_impar = input("Par ou Impar? ").strip().upper()[0]

    if par_impar not in "PI":
        print("Digite um valor válido")
        continue

    usuario = int(input("Escolha um numero: "))
    soma = usuario + computador

    if par_impar in "P" and soma % 2 == 0:
        print(f"usuario: {usuario} computador: {computador}. Vitória usuário")
        pontos_usuario += 1
        computador = random.randint(1, 10)

    elif par_impar in "I" and soma % 2 != 0:
        print(f"usuario: {usuario} computador: {computador}. Vitória usuário")
        pontos_usuario += 1
        computador = random.randint(1, 10)

    else:
        print(f"usuario: {usuario} computador: {computador}."
              "Vitória computador")
        break

print(f"usuario total vitorias: {pontos_usuario}")
