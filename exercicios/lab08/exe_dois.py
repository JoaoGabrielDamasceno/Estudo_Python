texto = input()
lista = texto.split()
letra = ''
lista_palavras = []
lista_numero = []
lista_hastag = []
lista_emoticon = []

for i in lista:
    letra = list(i)
    if i.isalpha():
        lista_palavras.append(i)
    elif (i[1:].isdigit() and i[0] == '-')  or (i.isdigit()):
            lista_numero.append(i)
    elif letra[0] == '#':
        lista_hastag.append(i)
    else:
        lista_emoticon.append(i)

lista_palavras.insert(0, 'Palavra(s):')
lista_palavras = ' '.join(lista_palavras)

lista_numero.insert(0, 'Numero(s):')
lista_numero = ' '.join(lista_numero)

lista_hastag.insert(0, 'Hashtag(s):')
lista_hastag = ' '.join(lista_hastag)

lista_emoticon.insert(0, 'Emoticon(s):')
lista_emoticon = ' '.join(lista_emoticon)

print(lista_palavras)
print(lista_numero)
print(lista_hastag)
print(lista_emoticon, end='')
