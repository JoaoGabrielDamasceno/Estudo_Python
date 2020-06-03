"""
Passado uma lista/tupla/dicionario(qualquer iteravel, string tb), verifica a quantidade de vezes dos elementos -> qtd vai ser o valor e o elemento a chave
"""
from collections import Counter

lista = [1,2,3,4,4,42,2,2,342,5,1,1,23,4,5,6,5,6,7,8]

rest = Counter(lista)

print(rest)

#EXEMPLO INTERESSANTE
texto = """Mestre na arte da vida faz pouca distinção entre o seu trabalho e o seu lazer, entre a sua mente e o seu corpo, entre a 
sua educação e a sua recreação, entre o seu amor e a sua religião. Ele dificilmente sabe distinguir um corpo do outro. 
Ele simplesmente persegue sua visão de excelência em tudo que faz, deixando para os 
outros a decisão de saber se está trabalhando ou se divertindo. Ele acha que está sempre fazendo as duas coisas simultaneamente.
"""

palavra = texto.split()

c_palavra = Counter(palavra)
print(c_palavra)

#ENCONTRANDO COM MAIS OCORRENCIA
print(c_palavra.most_common(4))