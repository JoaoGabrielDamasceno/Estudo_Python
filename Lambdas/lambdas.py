"""
Funções Lambdas são funções sem nome, ou seja, funções anônimas

FORMATO
lambda entrada: retorno
"""


exemplo = lambda x: x*3
y = input()
print(y)
print(exemplo(y))

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()
print(nome_completo('Joao   ', ' GABRIEL  '))

autores = ['Joao Gabriel', 'Joao Damasceno', 'Ana Silva', 'Carlos Botelho']
autores.sort(key= lambda sobrenome: sobrenome.split()[-1])
print(autores)