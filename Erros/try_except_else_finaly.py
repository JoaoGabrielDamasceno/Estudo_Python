"""
TRY/EXCEPT/ELSE/FINALLY

->Todo dado de entrada deve ser tratado

Não se deve tratar os erros na hora de entrar com os dados ou chamar a função e sim tratar os erros dentro das funções

"""
num = 0

try:
    num = int(input('Digite um número: '))
except ValueError:
    print('Você digitou um número inválido')
else:
    print(f'O número digitado foi {num}')
finally:
    print('Finally é sempre executado(Usado para fechar ou desalocar recursos!)')

#EXEMPLO COMPLEXO
def divide(a,b):
    try:
        return int(a)/int(b)
    except ValueError:
        return 'Entrada(s) inválida!'
    except ZeroDivisionError:
        return 'Não é possivel dividir por 0'
#DA PARA DIMINUIR ESSE CODIGO FAZENDO APENAS UM EXCEPT COM UMA TUPLA DOS DOIS ERROS (EXCEPT (VALUEERROR, ZERO...))

a = input('Digite o valor de a: ')
b = input('Digite o valor de b: ')

print(divide(a,b))