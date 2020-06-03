"""
O bloco try/except

Utilizamos esse bloco para tratar erros que podem ocorrer no código, prevenindo que o código pare de funcionar e o usúario receba uma mensagem de erro
inesperada.

Modelo ->
try:
    erro
execept:
    o que deve ser feito em caso de problema
"""

#TRATANDO O ERRO DE MANEIRA ESPECÍFICA
try:
    printf()
except NameError as err:
    print(f'A função foi digitada errada! Erro do tipo: {err}')


#USANDO COM FUNÇÃO
def pega_valor(dic, chave):
    try:
        return dic['chave']
    except ValueError:
        return None
    except TypeError:
        return None

dicio = {'nome', 'cor'}
print(pega_valor(dicio, 'azul'))
