"""
**kwarg
->Ao contrário do *args, tranforma os parametros extras em um dicionario

"""

def cores_favoritas(**kwargs):
    for chave, valor in kwargs.items():
        print(f'{chave.title()} gosta de {valor}')

cores_favoritas(marcos = 'vermelho')

"""
NAS FUNÇÕES DEFINIR OS PARAMETROS NESSA ORDEM

1° PARAMETROS OBRIGATORIOS
2° *ARGS
3° PARAMETROS DEFAULT
4° **KWARGS

def exemplo(a,b, *args, ex = 'x', **kwargs)
"""

#DESCOMPACTAR

def ex_desempacota(**kwargs):
    print(kwargs)


dicionario = {'nome' : 'joao'}
tupla = 1,2,3
ex_desempacota(**dicionario)

