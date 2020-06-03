"""
Dunder name -> __name__
Dunder main -> __main__

São usados dunder para criar funções, atributos e etc para não gerar confiltos com esses nomes na progamação 

if __named__ == '__main__':
    print('x')

Isso acima é importante ser usado por exemplo num módulo criado para que certa parte do código só seje executado naquele arquivo
visto que ao importar o módulo será executado o trecho de codigo que não estiver nessa condicional
"""