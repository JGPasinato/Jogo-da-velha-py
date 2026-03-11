tabuleiro = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

Jogador = "X"



def ExibeTabuleiro():
    for linha in tabuleiro:
        print(' | '.join(linha))
        print('-' * 6)


def jogada(linha,coluna):
    if tabuleiro[linha][coluna] != ' ':
        print('jogada invalida')
        return Jogador
    tabuleiro[linha][coluna] = Jogador
    return 'O' if Jogador == 'X' else  'X'
 

while True: 
    print(f'jogador da vez: {Jogador}')
    try:
        linha = int(input('Digite a linha: '))
        coluna = int(input('Digite a coluna: '))
        jogador = jogada(linha, coluna)
    except IndexError:
        print('Digite valores numéricos entre 0 e 2!')
    except ValueError:
        print('Os valores devem ser números inteiros!')
    ExibeTabuleiro()


#Jogador = jogada(1,1)
#Jogador = jogada(2,1)
#ExibeTabuleiro()

