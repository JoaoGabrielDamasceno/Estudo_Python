"""
Decorator são funções

-> Contém outras funções e aprimoram seus comportamentos
-> Tem uma sintaxe prórpia, utilizando '@'
"""

#DECORATOR FUNCTION
def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer conhecer voçê!')
        funcao()
        print('Tenha um bom dia')
    return sendo_mesmo

#DECORATOR
@seja_educado_mesmo
def dormir():
    print('Meu nome é pedro')

dormir()