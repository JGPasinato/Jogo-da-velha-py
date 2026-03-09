tabuleiro = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

Jogador = "X"



def ExibeTabuleiro():
    for linha in tabuleiro:
        print(' | '.join(linha))
        print('-' * 6)


def jogada(linha,coluna):
    tabuleiro[linha][coluna] = Jogador
    if Jogador == 'X':
      return 'O'
    else:
        return 'X'

Jogador = jogada(1,1)
Jogador = jogada(2,1)
ExibeTabuleiro()

