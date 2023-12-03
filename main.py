from termcolor import colored
from colorama import init

def exibir_tabuleiro(tabuleiro):
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == "X":
                print(colored(" X ", "red"), end="")
            elif tabuleiro[i][j] == "O":
                print(colored(" O ", "blue"), end="")
            else:
                print(colored(f" {i * 3 + j + 1} ", "white"), end="")

            if j < 2:
                print("|", end="")

        print()
        if i < 2:
            print("-" * 13)

def verificar_vitoria(tabuleiro, jogador):
    # Verificar linhas e colunas
    for i in range(3):
        if all([tabuleiro[i][j] == jogador for j in range(3)]) or all([tabuleiro[j][i] == jogador for j in range(3)]):
            return True

    # Verificar diagonais
    if all([tabuleiro[i][i] == jogador for i in range(3)]) or all([tabuleiro[i][2 - i] == jogador for i in range(3)]):
        return True

    return False

def start():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador_atual = "X"

    while True:
        exibir_tabuleiro(tabuleiro)
        escolha = input(f"Jogador {jogador_atual}, escolha uma posição (1-9): ")

        if escolha.isdigit():
            posicao = int(escolha) - 1
            linha, coluna = divmod(posicao, 3)

            if 0 <= linha < 3 and 0 <= coluna < 3 and tabuleiro[linha][coluna] == " ":
                tabuleiro[linha][coluna] = jogador_atual

                if verificar_vitoria(tabuleiro, jogador_atual):
                    exibir_tabuleiro(tabuleiro)
                    print(f"Jogador {jogador_atual} venceu!")
                    break

                if all([all([celula != " " for celula in linha]) for linha in tabuleiro]):
                    exibir_tabuleiro(tabuleiro)
                    print("Empate!")
                    break

                jogador_atual = "O" if jogador_atual == "X" else "X"
            else:
                print("Posição inválida. Tente novamente.")
        else:
            print("Entrada inválida. Insira um número de 1 a 9.")

if __name__ == "__main__":
    start()
