"""
Teoria dos conjuntos da Matemática
Conjuntos em Python são chamados de sets

-Não possui valores ordenados
-Não possui valores duplicados
-Não são acessados via indice ou seja não são indexados

-Importantes quando queremos armazenar dados que não nos importamos com a ordenação
-Representado por {}
-DIFERENÇA ENTRE CONJUNTO E DICIONÁRIOS(não é chave/valor e tem apenas valor)

"""

#DEFINIÇÃO 1 (Não coloca valores repetidos lembrando)
conjunto = {1,2,3,4,2,5,1}
print(conjunto)

conjunto2 = set({1,2,3,1,2,5})
print(conjunto)

#MESMA COISA COM TUPLA
lista = [1,2,3,5,4,7,8,5,6,1]
print(set(lista))

if 3 in conjunto:
    print("Está aqui!")

#DADOS MISTURADOS
conjunto2 = {1, 2, True, 'ola'}

"""
Pessoas vindas de cidades para um evento
"""

lista = ['São Paulo', 'Campinas', 'Matão', 'Matão']
print(lista)

#QUANTAS CIDADE DIFERENTES?
print(len(set(lista)))

#ADICIONANDO
conjunto.add(20)
print(conjunto)

#REMOVENDO 1 (GERA ERROR SE NÃO ENCONTRA)
conjunto.remove(20)
print(conjunto)

#REMOVENDO 2 (NÃO GERA ERROR SE NÃO ENCONTRAR)
conjunto.discard(4)
print(conjunto)

#DEEP COPY E SHALLOW COPY

#JUNTAR DOIS CONJUNTOS COM NOMES UNICOS --- UNION
alunosp = {'Joao', 'Julia', 'Marcos', 'Ana'}
alunosj = {'Joao','Pedro', 'Beatriz'}

unicos1 = alunosp.union(alunosj)
print(unicos1)

unicos2 = alunosp | alunosj

#ESTUDANTES QUE ESTÃO EM AMBOS
ambos1 = alunosp.intersection(alunosj)
print(ambos1)

ambos2 = alunosp & alunosj
print(ambos2)

#QUE ESTÃO NESSE CONJUNTO MAS NÃO NO OUTRO
so1 = alunosp.difference(alunosj)
print(so1)

