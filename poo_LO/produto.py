

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome 
        self.preco = preco

    
    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))

    # Getters

    @property
    def preco(self):
        return self._preco
    
    @property
    def nome(self):
        return self._nome
    
    # Setters

    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str): # verificando se o valor recebido é do 'tipo' string
            valor = float(valor.replace('R$', '')) # uma boa opção para esse tipo de verificação é utilizar expressões regulares
        self._preco = valor

    @nome.setter  
    def nome(self, name):
        self._nome = name.title()