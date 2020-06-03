"""
TUPLAS
->Representadas por ()
->São imutaveis ou seja, as operações não mudam elas mas criam uma nova
->Não existe então adição e subtração

USAR TUPLA QUANDO NÃO PRECISAMOS MODIFICAR DADOS DENTRO DE UMA COLEÇÃO
EX: MESES = ('JANEIRO', 'FEVEREIRO'...)

->TUPLAS SÃO MAIS RÁPIDAS QUE LISTAS
->DEIXAM SEU CODIGO MAIS SEGURO POR SEREM IMUTAVEIS
"""

tupla1 = (1, 2, 3, 4)

tupla2 = 1, 2, 3, 4

#CUIDADE tupla = (1) -> isso não é uma tupla

#ISSO É UMA TUPLA OU SEJA SÃO DEFINIDAS PELA VIRGULA E NÃO POR PARENTESES EM TESE
tupla3 = (1,)

#GERAR UMA TUPLA ATRAVÉS DO RANGE
tuplar = tuple(range(11))
print(tuplar)

tupla3 = ("Joao", "Damasceno")
nome, sobrenome = tupla3
print(nome)
print(sobrenome)

#SOMA, MAXIMO, MIN E TAMANHO (só se forem inteiros ou reias)

print(sum(tupla1))
print(max(tupla1))
print(min(tupla1))
print(len(tupla1))

print(tupla1 + tupla2)
print(tupla1)
print(tupla2)

tupla4 = tupla1 + tupla2
print(tupla4)
#OU
tupla1 = tupla1 + tupla2 #TUPLAS SÃO IMUTAVEIS PORÉM DA PRA SOBRESCREVER SEUS VALORES
print(tupla1)

print(1 in tupla1)

for n in tupla1:
    print(n)

for indice, valor in enumerate(tupla1):
    print(f'{indice}--{valor}')

tupla5 = 'a', 'b', 'b', 'a'
print(tupla5.count('a'))

print(tupla5[1])
print(tupla5.index('a'))
print(tupla5.index('a',1))
