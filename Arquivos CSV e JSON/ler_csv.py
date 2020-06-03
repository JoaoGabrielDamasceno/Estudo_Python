"""
CSV - Valores separados por vírgula

A linguagem Python possui duas formas diferentes para ajudar a ler arquivos CSV:
- Reader() permite que iteremos sob as linhas do arquivo CSV como listas
- DicReader permite que iteremos sob as linhas do arquivo CSV como OrderedDicts

#READER

from csv import reader

with open('original.csv', encoding='utf-8') as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv) #pula o cabeçalho
    for linhas in leitor_csv:
        #print(linhas)
        print(f'{linhas[0]} nasceu em {linhas[1]} e tem {linhas[2]} de altura')

"""

#DICREADER

from csv import DictReader

with open('original.csv', encoding='utf-8') as arquivo:
    leitor_csv = DictReader(arquivo, delimiter = ',')
    for linha in leitor_csv:
        #print(linha)
        print(f'{linha["Nome"]} nasceu no(a)(s) {linha["País"]} e tem {linha["Altura (em cm)"]}')


    
