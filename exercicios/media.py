def trata_dados(x):
    x = x[1:-1]
    x = x.split(",")
    um = float(x[0])
    dois = int(x[1])
    return um,dois

def media_lab(lista):
    total = 0
    d = 0
    final = 0
    for x in lista:
         total += x[0] * x[1]
         d += x[1]
    final = total/d
    
    return round(final, ndigits=1)
         
    


notas_lab = [trata_dados(x) for x in input().split()]
prova1, prova2 = [float(x) for x in input().split()]

media_lab = media_lab(notas_lab)
media_provas = (prova1*3 + prova2*4)/7

print(f'Media das tarefas de laboratorio: {media_lab}')
print(f'Media das provas: {round(media_provas, ndigits=1)}')

media_final = 0
meida_preliminar = 0

if media_provas >=5  and media_lab >=5:
    media_final =  0.7 * media_provas + 0.3 * media_lab
    print('Aprovado(a) por nota e frequencia')


elif media_provas >= 2.5  and media_lab >= 2.5:
    exame = float(input())
    media_preliminar = min(4.9, 0.7 * media_provas + 0.3 * media_lab)
    media_final = (media_preliminar + exame)/2
    print(f'Media preliminar: {round(media_preliminar, ndigits=1)}')
    print(f'Nota no exame: {exame}')

    if media_final >= 5:
        print('Aprovado(a) por nota e frequencia')
    else:
        print('Reprovado(a) por nota')

elif media_provas <= 2.5 or media_lab <= 2.5:
    print('Reprovado(a) por nota')
    media_final = min(media_lab, media_provas)

print(f'Media final: {round(media_final, ndigits=1)}', end='') 








