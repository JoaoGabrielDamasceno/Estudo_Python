"""
ESCOPO DE VARIAVEIS

Dois casos de escopo

1 - Variaveis globais (No programa todo)

2 - Variaveis locais (Só no bloco onde foi declarada)

"""

numero = 42

if numero>10:
    novo = numero + 10
    print(novo)

print(novo)

if numero<10:
    novo2 = numero - 10
    print(novo2)

#DA ERRO PORQUE NOVO2 NÃO FOI DECLARADO
#print(novo2)

def fund():
    x = 1
    y = 2

print(x)