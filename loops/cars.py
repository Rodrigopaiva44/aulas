# criar um programa que simula uma corrida entre dois carros, onde os carros
# avançam a cada iteração do loop. O carro A começa na posição 0 e o carro B
# começa na posição 0. Cada carro avança uma distância aleatória entre 1 e 5.
# O carro que atingir a posição de 30 primeiro é declarado vencedor.

import random


def main():
    position_a = 0
    position_b = 0

    while position_a < 30 and position_b < 30:
        # Avanço do carro A
        advance_a = random.randint(1, 5)
        position_a += advance_a

        # Avanço do carro B
        advance_b = random.randint(1, 5)
        position_b += advance_b

        print(f"Carro A avançou {advance_a} unidades. Posição: {position_a}")
        print(f"Carro B avançou {advance_b} unidades. Posição: {position_b}")
        print()

    if position_a >= 30:
        print("Carro A venceu a corrida!")
    else:
        print("Carro B venceu a corrida!")


if __name__ == "__main__":
    main()
