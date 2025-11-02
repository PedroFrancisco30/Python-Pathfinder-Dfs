import random
def aleatorizando_bloqueios(mapa,bloq,simbolo = '#'):
    """Função que serve par aleatorizar os bloqueios existentes"""
    
    linhas = len(mapa)
    colunas = len(mapa[0])
    if bloq > linhas*colunas:
        print("Mais minas que espaços disponiveis")
        exit()

    colocadas = 0
    #colocando os bloqueios de maneira aleatoria ao longo do mapa
    while colocadas < bloq:
        lin = random.randrange(linhas)
        col = random.randrange(colunas)
        if mapa[lin][col] == '-' and not (lin == 0 and col == 0) and not (lin == linhas-1 and col == colunas-1):
            mapa[lin][col] = simbolo
            colocadas += 1


def printar_mapa(mapa):
    for linha in mapa:
        print(' '.join(linha))
    print()

def andando_campo(mapa,direcoes,linha_n = 0,coluna_n = 0):
                        
    if not (0 <= linha_n < len(mapa)) or not (0 <= coluna_n < len(mapa[0])):
     return 0
    
    if mapa[linha_n][coluna_n] == '#' or mapa[linha_n][coluna_n] == '*':
        return 0

    if mapa[linha_n][coluna_n] == 'S':
        return 1    

    if mapa[linha_n][coluna_n] != 'R':
     mapa[linha_n][coluna_n] = '*'
    
    for dr ,dc in direcoes:
        nova_linha = linha_n + dr
        nova_coluna = coluna_n +dc
    
        if andando_campo(mapa,direcoes,nova_linha,nova_coluna):
            return 1
    
    if mapa[linha_n][coluna_n] != 'R':
        mapa[linha_n][coluna_n] = '-'
    return 0
    
"""Main do Codigo"""
while True:
    
    try:
        linhas = int(input("Quantas linhas terao na seu tabuleiro? "))
        if not linhas > 0:
            print("Coloque um numero valido de linhas")
            continue
        else:
            break
    except ValueError:
        print("Digite apenas caracteres validos")
        
    
while True:
    try:
        colunas = int(input("Quantas colunas terao no seu tabuleiro? "))
        if not colunas > 0:
            print("Coloque um numero valido de colunas")
            continue
        else:
            break
    except ValueError:
        print("Digite apenas caracteres validos")
    
while True:
    try:
        max_bloq = linhas*colunas - 2
        bloqueio = int(input(f"Quantos bloqueios voce quer no seu mapa?(Maximo{max_bloq})"))
        if bloqueio < 0 or bloqueio > max_bloq:
            print("Digite um numero valido de bloqueios")
        else:
            break
    except ValueError:
        print("Digite apenas caracteres validos")
        
campo = []
    
for i in range(linhas):
    linha = []
    for j in range(colunas):
        linha.append('-')
    campo.append(linha)
    
campo[0][0] = 'R'
campo[linhas -1][colunas -1] = 'S'
direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]

"""Chamando as funcoes e printando o mapa ja montado """
aleatorizando_bloqueios(campo,bloqueio,'#')
printar_mapa(campo)


if andando_campo(campo,direcoes):
    printar_mapa(campo)
    print("")
    print("Parabens voce ganhou")
else:
    printar_mapa(campo)
    print("VOCE PERDEU")