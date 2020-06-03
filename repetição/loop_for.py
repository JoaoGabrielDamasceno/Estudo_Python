"""
nome = 'Joao Gabriel'
lista = [1,3,5,7]
numeros = range(1,10)

for letra in nome:
    print(letra)


ENUMERATE faz um tupla (indice, valor)
for i, v in enumerate(nome):
    print(nome[i])

OU

for i, v in enumerate(nome):
    print(v)

OU descartando o indice

for _, v in enumerate(nome):
    print(v)
 
OU trazendo os dois valores juntos

for tupla in enumerate(nome):
    print(tupla)

qtd = int(input('I5nforme a quantidade de números a serem somados: '))
soma = 0


for n in range(1, qtd+1):
    numero = int(input(f'Informe o numero {n}/{qtd}: '))
    soma += numero
print(soma)

---SEM PULAR LINHA NO PRINT---
ola = "Joao Gabriel"
for letra in ola:
    print(letra, end='')

"""