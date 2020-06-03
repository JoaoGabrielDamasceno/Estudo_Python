import copy

#[linha][coluna]
def qtd_vivos(i,j):

    vivos = 0

    #print(f'na funcaoooo   {tabuleiro}')
    if tabuleiro[i-1][j+1] == "@":
        vivos += 1
    if tabuleiro[i-1][j] == "@":
        vivos += 1
    if tabuleiro[i-1][j-1] == "@":
        vivos += 1
    if tabuleiro[i][j+1] == "@":
        vivos += 1
    if tabuleiro[i][j-1] == "@":
        vivos += 1
    if tabuleiro[i+1][j+1] == "@":
        vivos += 1
    if tabuleiro[i+1][j] == "@":
        vivos += 1
    if tabuleiro[i+1][j-1] == "@":
        vivos += 1

    return vivos
 
def desenha_resultado():
    for i in tabuleiro:
        if(i != i[:-1]):
            print(' '.join(i))
        else:
            print(' '.join(i), end='')




c = True

tabuleiro = []
itera = 0

while c:

    entrada = input()
    entrada = list(entrada)

    try:
        itera = int(' '.join(entrada))
        c = False
        tabuleiro.append(entrada)
    except:
        tabuleiro.append(entrada)

itera = int(' '.join(tabuleiro.pop()))

n_linhas = len(tabuleiro)
n_colunas = len(tabuleiro[0])

tabuleiro_aux = copy.deepcopy(tabuleiro)

for i in range(0, len(tabuleiro)):
        v = 0
        linha = ''.join(tabuleiro_aux[i])
        print(linha)  


vezes = 0

while vezes < itera:
    for i in range(1, n_linhas-1):
        for j in range(1, n_colunas-1):
            total_vivos = qtd_vivos(i,j)
            if tabuleiro[i][j] == '@' and (total_vivos == 3 or total_vivos == 2):
                tabuleiro_aux[i][j] = '@'
            if tabuleiro[i][j] == '@' and (total_vivos > 3 or total_vivos < 2):
                tabuleiro_aux[i][j] = ' '
            if tabuleiro[i][j] == ' ' and (total_vivos == 3):
                tabuleiro_aux[i][j] = '@'

    for i in range(0, n_linhas):
        for j in range(0, n_colunas):
            tabuleiro[i][j] = tabuleiro_aux[i][j]
 
    vezes += 1

    for i in range(0, len(tabuleiro)):
        linha = ''.join(tabuleiro[i])
        if vezes == itera:
            if i==len(tabuleiro)-1:
                print(linha,end='')   
            else:
                print(linha)
        else:
            print(linha)