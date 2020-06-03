"""

DICIONÁRIOS (mapas)
---> Chave/Valor
---  Representado por "{}"
"""

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'ing': 'Inglaterra'}
print(paises)

#ACESSANDO ELEMENTOS

# 1° FORMA -> VIA CHAVE, IGUAL LISTA/TUPLA
print(paises['br'])

# 2° FORMA -> VIA GET (RECOMENDADO)
print(paises.get('br'))
print(paises.get('ru')) #PRINTA NONE E NÃO UM ERRO POR NÃO ENCONTRAR

#EXEMPLO
russia = paises.get('ru')
if russia:
    print('País encontrado!')
else:
    print('País não encontrado!')

# DA PARA FAZER DA SEGUINTE MANEIRA "russia = pais.get('ru', 'Pais não encontrado')" caso não encontre com a chave pedida, não retorna o valor None e sim a mensagem colocada

#BUSCA PELA CHAVE E NÃO PELO VALOR
print('br' in paises)
print('Estados Unidos' in paises)

#TUPLAS SÃO INTERESSANTES USAR COMO CHAVE PELO FATOR DE SEREM IMUTAVEIS
localidade = {
    (2, 3) : 'Minha casa',
    (5, 5) : 'Trabalho'
}

#ADICIONANDO --- NÃO DA PRA TER DUAS CHAVES IGUAIS POREM DA PARA TER VALORES REPITIDOS
# 1° FORMA (MAIS COMUM)
paises['ru'] = 'Russia'
print(paises)

# 2°FORMA
paises.update({'itl':'Italia'})
print(paises)

#REMOVENDO
# 1° FORMA (MAIS COMUM)
# QUANDO RETIRADO UM ELEMENTO SEMPRE SERÁ RETORNADO SEU VALOR
paises.pop('eua')
print(paises)

ret = paises.pop('ru')
print(ret)
print(paises)

# 2° FORMA
del paises['itl']
print(paises)

#PORQUE USAR DICIONARIOS?
#CARRINHO DE COMPRA COM ---LISTA---
carrinho = []
prod1 = ['Bala', 2, 2.50]
prod2 = ['Chocolate', 1, 3.56]

carrinho.append(prod1)
carrinho.append(prod2)

print(carrinho)

#COM TUPLA
carrinho = []
prod1 = ('Bala', 2, 2.50)
prod2 = ('Chocolate', 1, 3.56)

carrinho.append(prod1)
carrinho.append(prod2)

print(carrinho)

#USANDO DICIONARIO
carrinho = []
prod1 = {'nome': 'Bala', 'qtd' : 2, 'preço' : 2.50}
prod2 = {'nome': 'Chocolate', 'qtd': 1, 'preco' : 3.59}

carrinho.append(prod1)
carrinho.append(prod2)

print(carrinho)

# ALGUNS MÉTODOS DE DICIONARIOS
prod1.clear()
print(prod1)

# DEEP COPY
prod3 = prod2.copy()
prod3['peso'] = '80g'
print(prod3)

# SHALLOW COPY
prod4 = prod2
prod4['peso'] = '74g'
print(prod4)
print(prod2)

print(carrinho)

#FORMA NÃO USUAL MAS INTERESSANTE
usuario = {}.fromkeys(['nome', 'idade', 'peso'], 'desconhecido')
print(usuario)

