class Contador:
    def __init__(self, menor, maior):
        self.menor = menor
        self.maior = maior
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.menor < self.maior:
            numero = self.menor
            self.menor = numero + 1
            return numero
        raise StopIteration

for i in Contador(1,10):
    print(i)