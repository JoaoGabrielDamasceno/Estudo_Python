"""
Levantando os próprios erros com raise

Raise -> Lança exceçõs

Não é uma função, apenas uma palavra reservada

Raise assim como o return finaliza a função
"""

#EXEMPLO
def texto(nome,cor):
    cores = ['azul', 'verelho']
    if type(nome) is not str:
        raise TypeError('Não é um nome')
    if type(cor) is not str:
        raise TypeError('Não é uma cor')
    if cor not in cores:
        raise ValueError('Essa cor não existe!')
    print(f'{nome} gosta da cor {cor}')

texto('Joao', 'amarelo')
#texto('Joao', 3)