from random import choice
from time import sleep

answer = 'S'
win = draw = loss = 0

while answer == "S":
    print('''SUAS OPÇÕES: 
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')

    player = int(input("Qual a sua jogada? "))

    if player in [0, 1, 2]:
        if player == 0:
            player = 'Pedra'
        elif player == 1:
            player = "Papel"
        elif player == 2:
            player = "Tesoura"

        computer = choice(['Pedra', 'Papel', 'Tesoura'])

        print("JO")
        sleep(1)
        print("KEN")
        sleep(1)
        print("PO!!!")

        print("=" * 25)
        print(f"Computador jogou {computer}")
        print(f"Jogador jogou {player}")
        print("=" * 25)

        # Jogador vence
        if player == 'Pedra' and computer == 'Tesoura':
            print("JOGADOR VENCE")
            win += 1
        elif player == 'Papel' and computer == 'Pedra':
            print("JOGADOR VENCE")
            win += 1
        elif player == 'Tesoura' and computer == 'Papel':
            print("JOGADOR VENCE")
            win += 1

        # Empate
        if player == computer:
            print("EMPATE")
            draw += 1

        # Computador vence
        if computer == 'Pedra' and player == 'Tesoura':
            print("COMPUTADOR VENCE")
            loss += 1
        elif computer == 'Papel' and player == 'Pedra':
            print("COMPUTADOR VENCE")
            loss += 1
        elif computer == 'Tesoura' and player == 'Papel':
            print("COMPUTADOR VENCE")
            loss += 1
    else:
        print("JOGADA INVÁLIDA")
    
    answer = str(input("Quer continuar? [S/N] ")).strip().upper()[0]

print("Seu desempenho:")
print(f"{win} Vitórias")
print(f"{draw} Empates")
print(f"{loss} Derrotas")
