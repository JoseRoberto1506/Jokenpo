def main():
    vitorias, empates, derrotas = 0, 0, 0
    while True:
        mostar_opcoes()

        jogada = int(input("Qual a sua jogada? "))
        if 0 <= jogada <= 2:
            resultado = jogar(jogada)
            # Atualizando variáveis de desempenho
            if resultado == "v":
                vitorias += 1
            elif resultado == "e":
                empates += 1
            else:
                derrotas += 1
        else:
            print("JOGADA INVÁLIDA")
        
        resposta = str(input("\nQuer continuar? [S/N] ")).strip().upper()[0]
        if resposta != "S":
            desempenho(vitorias, empates, derrotas)
            break


def mostar_opcoes():
    print('''\nSUAS OPÇÕES: 
    [ 0 ] Pedra
    [ 1 ] Papel
    [ 2 ] Tesoura''')


def jogar(jogada_usuario):
    from random import randint
    from time import sleep

    opcoes = ['Pedra', 'Papel', 'Tesoura']
    jogada_computador = randint(0, 2)

    print("JO")
    sleep(1)
    print("KEN")
    sleep(1)
    print("PO!!!")

    print(f"Computador jogou {opcoes[jogada_computador]}")
    print(f"Jogador jogou {opcoes[jogada_usuario]}")

    # Jogador vence
    if jogada_usuario == 0 and jogada_computador == 2: # Pedra x Tesoura
        print("JOGADOR VENCE")
        return "v"
    elif jogada_usuario == 1 and jogada_computador == 0: # Papel x Pedra
        print("JOGADOR VENCE")
        return "v"
    elif jogada_usuario == 2 and jogada_computador == 1: # Tesoura x Papel
        print("JOGADOR VENCE")
        return "v"

    # Empate
    if jogada_usuario == jogada_computador:
        print("EMPATE")
        return "e"

    # Computador vence
    if jogada_computador == 0 and jogada_usuario == 2: # Pedra x Tesoura
        print("COMPUTADOR VENCE")
        return "d"
    elif jogada_computador == 1 and jogada_usuario == 0: # Papel x Pedra
        print("COMPUTADOR VENCE")
        return "d"
    elif jogada_computador == 2 and jogada_usuario == 1: # Tesoura x Papel
        print("COMPUTADOR VENCE")
        return "d"


def desempenho(tot_vitorias, tot_empates, tot_derrotas):
    print("\nSeu desempenho:")
    print(f"{tot_vitorias} Vitórias")
    print(f"{tot_empates} Empates")
    print(f"{tot_derrotas} Derrotas\n")


main()