"""
Cria um iteravel chamado zip iteravel que agrega cada elemento de entrada dos iteraveis passado como entrada em pares
Utiliza o menor valor entre os iteraveis, ou seja, para quando o menor iteravel acabar
"""

lista1 = [1,2,3]
lista2 = [2,4,6]

zip1 = zip(lista1, lista2)
print(list(zip1))

#Lista de tuplas

l_t = [(1,2), (3,4), (5,6)]
print(list(zip(*l_t)))

#Exemplo mais complexo

prova1 = [8,9,10]
prova2 = [5,6,8]
alunos = ['Joao', 'Maria', 'Ana']

final = {dados[0]:max(dados[1], dados[2]) for dados in zip(alunos, prova1, prova2)}
print(final)

#COM MAP

final = zip(alunos, map(lambda notas: max(notas), zip(prova1, prova2)))
print(list(final))
