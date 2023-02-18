#!/usr/bin/env python3
# -*- codificacao: utf-8 -*-
"""
Created on Sun Sep 23 15:33:59 2018
@author: talles medeiros, decsi-ufop
"""

"""
Este código servirá de exemplo para o aprendizado do algoritmo MINIMAX 
na disciplina de Inteligência Artificial - CSI457
Semestre: 2018/2
"""

#!/usr/bin/env python3
from math import inf as infinity
from random import choice
import platform
import time
from os import system

"""
Um versão simples do algoritmo MINIMAX para o Jogo da Velha.
"""

# Representando a variável que identifica cada jogador
# HUMANO = Oponente humano
# COMP = Agente Inteligente
# tabuleiro = dicionário com os valores em cada posição (x,y)
# indicando o jogador que movimentou nessa posição.
# Começa vazio, com zero em todas posições.
HUMANO = -1
COMP = +1
#FAZER TABULEIRO 8x8
tabuleiro = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    ['R', 'R', 'R', 0, 0, 'R', 'R', 'R'],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 'G', 0, 0, 0, 0],

]
posicao_gato = [7,3]
posicao_rato = [[1,0], [1,1], [1,2], [1,4], [1,5], [1,6],[1,7]]

"""
Funcao para avaliacao heuristica do estado.
:parametro (estado): o estado atual do tabuleiro
:returna: +1 se o computador vence; -1 se o HUMANOo vence; 0 empate
 """
def avaliacao(estado):
    
    if vitoria(estado, COMP):
        placar = +1
    elif vitoria(estado, HUMANO):
        placar = -1
    else:
        placar = 0

    return placar
""" fim avaliacao (estado)------------------------------------- """

def vitoria(estado, jogador):
    """
    Esta funcao testa se um jogador especifico vence. Possibilidades:
    * Tres linhas     [X X X] or [O O O]
    * Tres colunas    [X X X] or [O O O]
    * Duas diagonais  [X X X] or [O O O]
    :param. (estado): o estado atual do tabuleiro
    :param. (jogador): um HUMANO ou um Computador
    :return: True se jogador vence
    """
    win_estado = [      
        [estado[7][0]],
        [estado[7][1]],
        [estado[7][2]],
        [estado[7][3]],
        [estado[7][4]],
        [estado[7][5]],
        [estado[7][6]],
        [estado[7][7]],
        
    ]
    # Se um, dentre todos os alinhamentos pertence um mesmo jogador, 
    # então o jogador vence!
    # if [jogador, jogador, jogador] in win_estado:
    if [jogador] in win_estado:

        return True
    else:
        return False
""" ---------------------------------------------------------- """

"""
Testa fim de jogo para ambos jogadores de acordo com estado atual
return: será fim de jogo caso ocorra vitória de um dos jogadores.
"""
def fim_jogo(estado):
    return vitoria(estado, HUMANO) or vitoria(estado, COMP)
""" ---------------------------------------------------------- """

"""
Verifica celular vazias e insere na lista para informar posições
ainda permitidas para próximas jogadas.
"""
def celulas_vazias(estado):
    celulas = []
    for x, row in enumerate(estado):
        for y, cell in enumerate(row):
            if cell == 0: celulas.append([x, y])
    return celulas
""" ---------------------------------------------------------- """

"""
Um movimento é valido se a célula escolhida está vazia.
:param (x): coordenada X
:param (y): coordenada Y
:return: True se o tabuleiro[x][y] está vazio
"""
def movimento_valido(i, j, jogador):
    global posicao_gato
    #print(posicao_gato)
    if jogador == 'HUMANO':
        
        if i == posicao_gato[0] and posicao_gato[1] < j: #move na direita
       
            for b in range(posicao_gato[1], j+1): 
                               
                if tabuleiro[posicao_gato[0]][b] != 'R' and b < j + 1: 
                    tabuleiro[posicao_gato[0]][posicao_gato[1]] = 0                   
                    posicao_gato = [i,b]                    
                    tabuleiro[i][b] = 'G'
                    limpa_console()
                    exibe_tabuleiro(tabuleiro)
                    time.sleep(0.5)

                elif tabuleiro[posicao_gato[0]][b] == 'R': #captura o rato
                    tabuleiro[posicao_gato[0]][posicao_gato[1]] = 0
                    posicao_gato = [i,b]                    
                    tabuleiro[i][b] = 'G'
                    limpa_console()
                    exibe_tabuleiro(tabuleiro)
                    time.sleep(0.5)
                    break

        elif i == posicao_gato[0] and posicao_gato[1] > j: #move na esquerda
                        
            for b in range(posicao_gato[1], j-1, -1): 
                               
                if tabuleiro[posicao_gato[0]][b] != 'R' and b > j-1: 
                    tabuleiro[posicao_gato[0]][posicao_gato[1]] = 0                   
                    posicao_gato = [i,b]                    
                    tabuleiro[i][b] = 'G'
                    limpa_console()
                    exibe_tabuleiro(tabuleiro)
                    time.sleep(0.5)

                elif tabuleiro[posicao_gato[0]][b] == 'R': #captura o rato
                    tabuleiro[posicao_gato[0]][posicao_gato[1]] = 0
                    posicao_gato = [i,b]                    
                    tabuleiro[i][b] = 'G'
                    limpa_console()
                    exibe_tabuleiro(tabuleiro)
                    time.sleep(0.5)
                    break
                    
        elif j == posicao_gato[1] and posicao_gato[0] > i: #move para cima
            
            for b in range(posicao_gato[0], i - 1, -1):
                
                if tabuleiro[b][posicao_gato[1]] != 'R' and b > i-1: 
                    tabuleiro[posicao_gato[0]][posicao_gato[1]] = 0                   
                    posicao_gato = [b,j]                    
                    tabuleiro[b][j] = 'G'
                    limpa_console()
                    exibe_tabuleiro(tabuleiro)
                    time.sleep(0.5)

                elif tabuleiro[b][posicao_gato[1]] == 'R': #captura o rato
                    tabuleiro[posicao_gato[0]][posicao_gato[1]] = 0                   
                    posicao_gato = [b,j]                    
                    tabuleiro[b][j] = 'G'
                    limpa_console()
                    exibe_tabuleiro(tabuleiro)
                    time.sleep(0.5)
                    break

        elif j == posicao_gato[1] and posicao_gato[0] < i: #move para baixo
            
            for b in range(posicao_gato[0], i+1):
                
                if tabuleiro[b][posicao_gato[1]] != 'R' and b < i+1: 
                    tabuleiro[posicao_gato[0]][posicao_gato[1]] = 0                   
                    posicao_gato = [b,j]                    
                    tabuleiro[b][j] = 'G'
                    limpa_console()
                    exibe_tabuleiro(tabuleiro)
                    time.sleep(0.5)

                elif tabuleiro[b][posicao_gato[1]] == 'R': #captura o rato
                    tabuleiro[posicao_gato[0]][posicao_gato[1]] = 0                   
                    posicao_gato = [b,j]                    
                    tabuleiro[b][j] = 'G'
                    limpa_console()
                    exibe_tabuleiro(tabuleiro)
                    time.sleep(0.5)
                    break
        else: 
            return False
    
    return True         


            
""" ---------------------------------------------------------- """

"""
Executa o movimento no tabuleiro se as coordenadas são válidas
:param (x): coordenadas X
:param (y): coordenadas Y
:param (jogador): o jogador da vez
"""
def exec_movimento(x, y, jogador):
    
    if movimento_valido(x, y, jogador):        
        
        return True
    else:
        return False
""" ---------------------------------------------------------- """

"""
Função da IA que escolhe o melhor movimento
:param (estado): estado atual do tabuleiro
:param (profundidade): índice do nó na árvore (0 <= profundidade <= 9),
mas nunca será nove neste caso (veja a função iavez())
:param (jogador): um HUMANO ou um Computador
:return: uma lista com [melhor linha, melhor coluna, melhor placar]
"""
def minimax(estado, profundidade, jogador):

    # valor-minmax(estado)
    if jogador == COMP:
        melhor = [-1, -1, -infinity]
    else:
        melhor = [-1, -1, +infinity]

    # valor-minimax(estado) = avaliacao(estado)
    if profundidade == 0 or fim_jogo(estado):
        placar = avaliacao(estado)
        return [-1, -1, placar]

    for cell in celulas_vazias(estado):
        x, y = cell[0], cell[1]
        estado[x][y] = jogador
        placar = minimax(estado, profundidade - 1, -jogador)
        estado[x][y] = 0
        placar[0], placar[1] = x, y

        if jogador == COMP:
            if placar[2] > melhor[2]:
                melhor = placar  # valor MAX
        else:
            if placar[2] < melhor[2]:
                melhor = placar  # valor MIN
                
    return melhor
""" ---------------------------------------------------------- """

"""
Limpa o console para SO Windows
"""
def limpa_console():
    os_name = platform.system().lower()
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')
    
""" ---------------------------------------------------------- """

"""
Imprime o tabuleiro no console
:param. (estado): estado atual do tabuleiro
"""
def exibe_tabuleiro(estado):
    j = 0;
    #print('-----------------------------------------')
    print(' | 0 || 1 || 2 || 3 || 4 || 5 || 6 || 7 |')
    
    for row in estado:
        print (j, end = "")
        j += 1
        for cell in row:
            
            if cell == 'G':
                print('| G |', end='')
            elif cell == 'R':
                print('| R |', end='')
            else:
                print('|', ' ', '|', end='')
        print('')
    
""" ---------------------------------------------------------- """

"""
Chama a função minimax se a profundidade < 9,
ou escolhe uma coordenada aleatória.
:param (comp_escolha): Computador escolhe X ou O
:param (humano_escolha): HUMANO escolhe X ou O
:return:
"""
def IA_vez():
    profundidade = len(celulas_vazias(tabuleiro))
    if profundidade == 0 or fim_jogo(tabuleiro):
        return

    limpa_console()
    print('Vez do Computador [{}]'.format(comp_escolha))
    exibe_tabuleiro(tabuleiro, comp_escolha, humano_escolha)

    if profundidade == 9:
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
    else:
        move = minimax(tabuleiro, profundidade, COMP)
        x, y = move[0], move[1]

    exec_movimento(x, y, COMP)
    time.sleep(1)
""" ---------------------------------------------------------- """


def HUMANO_vez():
    
    limpa_console()
    print('Vez do HUMANO [{}]')
    exibe_tabuleiro(tabuleiro)
    movimento = 1
    while (movimento == 1):
        try:
            linha = int(input('Escolha um numero (0..7) para linha: '))
            coluna = int(input('Escolha um numero (0..7) para coluna: '))            
            tenta_movimento = exec_movimento(linha, coluna, 'HUMANO')

            if tenta_movimento == False:
                print('Movimento Inválido')
                time.sleep(2)
                movimento = -1
        except KeyboardInterrupt:
            print('Tchau!')
            exit()
        except:
            print('Escolha Inválida!')
""" ---------------------------------------------------------- """

"""
Funcao Principal que chama todas funcoes
"""
def main():

    limpa_console()
    
    primeiro = ''  # se HUMANO e o primeiro
   
    # HUMANO pode começar primeiro
    limpa_console()
    exibe_tabuleiro(tabuleiro)
    
    while primeiro != 'S' and primeiro != 'N':
        try:
            primeiro = input('Primeiro a Iniciar?[s/n]: ').upper()
        except KeyboardInterrupt:
            print('Tchau!')
            exit()
        except:
            print('Escolha Errada!')

    # Laço principal do jogo
    while not fim_jogo(tabuleiro):
        if primeiro == 'N':
            IA_vez()
            primeiro = ''

        HUMANO_vez()
        
        #IA_vez()

    # Mensagem de Final de jogo
    if vitoria(tabuleiro, HUMANO):
        limpa_console()
        print('Vez do HUMANO [{}]'.format(humano_escolha))
        exibe_tabuleiro(tabuleiro, comp_escolha, humano_escolha)
        print('Você Venceu!')
    elif vitoria(tabuleiro, COMP):
        limpa_console()
        print('Vez do Computador [{}]'.format(comp_escolha))
        exibe_tabuleiro(tabuleiro, comp_escolha, humano_escolha)
        print('Você Perdeu!')
    else:
        limpa_console()
        exibe_tabuleiro(tabuleiro, comp_escolha, humano_escolha)
        print('Empate!')

    exit()

if __name__ == '__main__':
    main()
