"""
Métodos Get e Set para pegar e alteral os valores respectivamente. (NÃO SÃO USUAIS EM PYTHON)

   def get_nome(self):
        return f'{self.__nome}'

    def set_nome(self, nome):
        self.__nome = nome


---> NO PYTHON USAMOS PROPERTYS

     @property

"""

class Pessoa():

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome


    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


p1 = Pessoa('Joao', 'Damasceno', 46301237846)
print(p1.nome)
p1.nome = 'Gabriel'
print(p1.nome)