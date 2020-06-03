"""
Atributos de Instancia: Atributos declarados dentro do construtor
Atributos de Classe: Todos objetos criados a partir daquela classe terão naquele atributo o mesmo valor
Atributos Dinâmicos: Criados em tempo de execução

-> Todo atributo de um classe é público

-> Para demonstrar por conversão que um atributo é privado devemos usar "__" antes do nome do atributo
   Porém isso não impede que o atributo não seja acessado fora da classe

-> 'self' diz respeito ao objeto que está sendo executado

"""

#Atributos de Instancia

class Lampada:

    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligado = True

class Acesso:

    def __init__(self, email, senha):
        self.__email = email
        self.__senha = senha


#Atributos de Classe

class Produto:

    imposto = 1.05
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id 

p1 = Produto('Banana', 'Comestivel', 2.99)
print(p1.valor)

print(p1.id)

# ATRIBUTO DINAMICO

p1.peso = "4.5kg"

print(p1.peso)

del p1.peso
del p1.descricao

print(p1.__dict__)