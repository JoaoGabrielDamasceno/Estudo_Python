"""
->Parametro como outro qualquer, pode chamar de qualquer coisa desde que comece com * (por exemplo "*x" mas a comunidade definiu como padrão "*args")

->Coloca os paramêtros extras passados em uma tupla
"""

def soma(*args):
    return sum(args)

print(soma())
print(soma(2,3,43))
print(soma(2,3,4))

lista = [1,2,3,4,5]

print(soma(*lista)) #DESEMPACOTAMENTO DA LISTA, SE NÃO IRA PASSAR COMO UM ÚNICO ELEMENTO DA TUPLA