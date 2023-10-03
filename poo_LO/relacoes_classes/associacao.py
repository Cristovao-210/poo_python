"""
Associação -> As classes se relacionam, mas são independentes. Uma não depende em nada da outra.

"""

class Escritor:
    def __init__(self, nome):
        self.__nome = nome
        self.__ferramenta = None

    @property
    def ferramenta(self):
        return self.__ferramenta
    
    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta

    @property
    def nome(self):
        return self.__nome
    

class Caneta:
    def __init__(self, marca):
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca
    
    def escrever(self):
        print('Caneta escrevendo...')
    
    
class MaquinaDeEscrever:
    def escrever(self):
        print('Máquina sendo utilizada...')