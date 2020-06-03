"""
Funções das classes que representam o comportamento dos objetos

-> Metodos de Instancia: Metodos que precisam fazer acesso a atributos de instancia
-> Metodos de Classe: Acesso a atributos de classe

__init__ é o método chamado de construtor
"""

class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = True

class ContaCorrente:

    contador = 4999

    def __init__(self, numero, limite, saldo):
        self.__numero = numero
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero

class Produto:

    contador = 0

    #METODO DE CLASSE
    @classmethod
    def qtd_produtos(cls):
        return f'Temos {cls.contador} produtos registrados no sistema!'

    #MÉTODO ESTATICO
    @staticmethod
    def ver():
        return 'XSDSADA'

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id
        print(f'Produto {self.__nome} criado!')

    def desconto(self, porcentagem):
        """ Retorna o valor do produto com desconto"""
        return(self.__valor * (100 - porcentagem)/100)

class Usuario:

    def __init__(nome, email, senha):
        self.__nome = nome
        self.__email = email
        self.__senha = senha


p1 = Produto('PS2', 'Video Game', 1000)
print(p1.desconto(50))

print(Produto.qtd_produtos())