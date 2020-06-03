#EXEMPLO
def potencia(num, elevado=2):
    return num ** elevado

print(potencia(2))

#OU SEJA, NÃO PRECISA DIGITAR O SEGUNDO ARGUMENTO VISTO QUE POR PADÃO ELE VAI SER ELEVADO AO QUADRADO
#ESSES VALORES DEVEM IR AO FINAL DA DECLARAÇÃO 

def soma(n1,n2):
    return n1 + n2

def sub(n1,n2):
    return n1 - n2

def mat(n1, n2, fun = soma):
    return fun(n1,n2)

print(mat(1,2))
print(mat(1,2,sub))

#VARIAVEIS LOCAIS TEM PRIORIDADE DO QUE GLOBAL
ola = 'JOAO'

def oi():
    ola = 'PEDRO'
    print(ola)


#EVITE VARIAVEIS GLOBAIS
total = 0

def inc():
    global total
    total = total + 1
    return total

print(inc())
print(inc())