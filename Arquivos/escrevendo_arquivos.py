"""
Open('nome do arquivo','w' ) -> função utilizada para escrever em arquivos

Da mesma forma que quando se abre um arquivo para leitura só da para ler ele, na escrita a mesma coisa

Write() -> para escrever no arquivo aberto

"""

with open('novo.txt', 'w') as arquivo:
    arquivo.write('Ola.\n')
    arquivo.write('Escrevendo em um arquivo')

with open('fruta.txt', 'w') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou digite sair: ')
        if fruta != 'sair':
            arquivo.write(fruta + '\n')
        else:
            break