"""

from csv import writer

with open('filme.csv', 'w') as arquivo:
    escrito_csv = writer(arquivo)
    nome = None
    escrito_csv.writerow(['Nome', 'Gênero', 'Duração'])
    while nome != 'sair':
        nome = input('Informe o nome do filme: ')
        if nome != 'sair':
            genero = input('Informe o genero: ')
            duracao = input('Duracao: ')
            escrito_csv.writerow([nome,genero,duracao])

"""
from csv import DictWriter

with open('filme.csv', 'w') as arquivo:
    cabecalho = ['Nome', 'Genero', 'Duracao']
    escrito_csv = DictWriter(arquivo, fieldnames=cabecalho)
    escrito_csv.writeheader()
    nome = None
    while nome != 'sair':
        nome = input('Informe o nome do filme: ')
        if nome != 'sair':
            genero = input('Informe o genero: ')
            duracao = input('Duracao: ')
            escrito_csv.writerow({'Nome': nome, 'Genero': genero, 'Duracao': duracao}) 