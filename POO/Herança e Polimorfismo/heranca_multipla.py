"""
Um classe filha herdar de mais de um classe.

 - Multiderivação Direta
    class Classe1():
        pass

    class Classe2():
        pass


    class Herda(Classe1, Classe2):
        pass


 - Multiderivação Indireta

    class Classe1():
        pass

    class Classe2(Classe1):
        pass


    class Classe3(Classe2):
        pass

    
OBS: Não tem diferença, apenas de nomenclatura

"""

class Animal():

    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f'Eu sou {self.__nome}'

class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'O {self._Animal__nome} está nadando!'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} do mar!'

class Terrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'O {self._Animal__nome} está andando!'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} da terra!'    

class Pinguim(Aquatico, Terrestre):

    def __init__(self, nome):
        super().__init__(nome)

tux = Pinguim('Tux')
print(tux.andar())
print(tux.nadar())
print(tux.cumprimentar()) #ELE EXECUTA O METODO DO AQUATICO POR CAUSA DO MRO, ONDE O AQUATICO VEM ANTES NA DEFINIÇÃO DAS HERANÇAS DA CLASSE PENGUIM

#MRO É A RESOLUÇÃO DO METÓDO QUE DEVE SER ORGANIZADO PRIMEIRO