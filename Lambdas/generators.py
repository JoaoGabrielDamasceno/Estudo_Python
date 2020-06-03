"""
Tuple comprehensions seriam os Generators

nomes = ['Joao', 'Juliana', 'Joaquim']
print(all(nome[0].lower()== 'j' for nome in nomes))

Ocupa menos recurso e memória do que o list comprehension
Porque?
Pois quando você executa ele, não monta definitavemente, ele fica preparado para montar e quando monta já apaga da memória
já os outros como list,set, dict comprehensions já são montados
"""
nomes = ['Joao', 'Juliana', 'Joaquim']
res = (nome[0]=='J' for nome in nomes)
print(res)