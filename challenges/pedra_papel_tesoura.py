# Crie um pedra papel tesoura


from random import randint
from time import sleep
game = ["ROCK", "PAPER", "SCISSORS"]
scoreboard = 0
score_player = 0
score_computer = 0
draw = 0

# Game Loop
while True:
    sleep(1)
    computer = randint(0, 2)

    # Match Point
    if scoreboard == 5:
        print('THE GAME IS OVER')
        break
    try:
        player = int(input(
            "[0] ROCK\n"
            "[1] PAPER\n"
            "[2] SCISSORS\n"
            "> "))
    except ValueError:
        print("A LETTER WAS DIGITED! COMPUTER WINS")
        score_computer += 99
        break

    # Checking if player move's OK
    if player > 2 or player < 0:
        print("INVALID NUMBER! COMPUTER WINS!")
        score_computer = 99
        break

    # Game
    print(f'PLAYER: {game[player]}')
    print(f'COMPUTER: {game[computer]}')
    print("-----------------")

    # Player's point
    if ((player == 0 and computer == 2) or (player == 1 and computer == 0)
            or (player == 2 and computer == 1)):
        print('PLAYER WINS')
        score_player += 1

    # Computer's point
    elif (computer == 0 and player == 2 or computer == 1 and player == 0
            or computer == 2 and player == 1):
        print('COMPUTER WINS')
        score_computer += 1

    # Draw
    else:
        print("DRAW")
        draw += 1
    print("-----------------")
    scoreboard += 1


# SCOREBOARD
print("-----------------")
print("SCOREBOARD")
print(f'Player: {score_player}')
print(f'Computer: {score_computer}')
print(f'Draw: {draw}')
