def desenha(tipo, caract, dim):
    if tipo == 'Q':
        for i in range(dim):
            if i == (dim - 1): 
                print(dim * caract, end='')
            else:
                print(dim * caract)

    elif tipo == 'T':
        contador_espaco = dim
        contador_caract = 1
        for i in range(dim):
            if i == (dim - 1): 
               print(contador_caract * caract, end='')
            else:
                contador_espaco -= 1
                print(' ' * (contador_espaco), end='')
                print(contador_caract * caract)
                contador_caract += 2

    elif tipo == 'L':
        contador_espaco = dim
        contador_caract = 1
        metade = False
        for i in range(dim*2 -1):
            if i == (dim-1): 
               print(contador_caract * caract)
               metade = True
               contador_espaco -= 1
               contador_caract -= 2
            else:
                if metade:
                    contador_espaco += 1
                else:
                    contador_espaco -= 1
                print(' ' * (contador_espaco), end='')
                print(contador_caract * caract)

                if metade:
                    contador_caract -= 2
                else:
                    contador_caract += 2

    elif tipo == 'O':
        contador_espaco = dim
        contador_caract = dim
        metade = False
        for i in range(dim*2 -1):
            if i == (dim-1):
               for j in range(dim):
                    print(contador_caract * caract)
               metade = True
               contador_espaco -= 1
               contador_caract -= 2
            else:
                if metade:
                    contador_espaco += 1
                else:
                    contador_espaco -= 1
                print(' ' * (contador_espaco), end='')
                print(contador_caract * caract)

                if metade:
                    contador_caract -= 2
                else:
                    contador_caract += 2

    elif tipo == 'H':
        contador_espaco = dim
        contador_caract = dim
        metade = False
        for i in range(dim*2 -1):
            if i == (dim-1): 
               print(contador_caract * caract)
               metade = True
               contador_espaco -= 1
               contador_caract -= 2
            else:
                if metade:
                    contador_espaco += 1
                else:
                    contador_espaco -= 1
                print(' ' * (contador_espaco), end='')
                print(contador_caract * caract)

                if metade:
                    contador_caract -= 2
                else:
                    contador_caract += 2


objetos = ['Q', 'T', 'L', 'H', 'O']

tipo_objeto = input()
caracter = input()
dim = int(input())


if not tipo_objeto in objetos:
    print('Identificador invalido.')
elif (not dim >= 3):
    print('Dimensao invalida.')
else:
    desenha(tipo_objeto, caracter, dim)





