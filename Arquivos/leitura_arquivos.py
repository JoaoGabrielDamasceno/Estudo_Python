"""
Leitura

Utiliza a função open()

Na forma mais simples se passa apenas um parâmetro de entrada, que será o caminho do arquivo a ser utilizado

"""

#EXEMPLO

arquivo = open('texto_exemplo.txt')

#print(arquivo)

#Função READ() lê todo o conteúdo do arquivo, essa função retorna uma string que seria todo o texto
#print(arquivo.read())
ret = arquivo.read()
ret = ret.split(' ')
print(ret)

#Se tentar dar read de novo não funciona pois o python trabalha com uma espécie de cursor ou seja, ele vai ler a partir de onde parou