"""
Herança é a ideia de reaproveitar código, extender nossas classes

Uma nova classe passa a herdar atributos e métodos de outra classe.

"""

class Pessoa():

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):

    def __init__(self,nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda

c1 = Cliente('Joao', 'Gabriel', '557505550', '0')

print(c1.nome_completo())
print(c1.__dict__)