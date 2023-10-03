"""
Dentro da associação existe a agregação e a composição
São relações de todo/parte. Uma Classe usa a outra como parte de si.

AGREGAÇÃO: É o tipo de relação em que uma classe não funciona adequadamente se não tiver a outra como parte.

"""

class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def inserir_produto(self, produto):
        self.produtos.append(produto)

    def lista_produto(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)

    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return total

class Produto:
    def __init__(self, nome, valor):
        self.nome = nome 
        self.valor = valor 

# a classe é instânciada, mas no momento não tem produtos
carrinho = CarrinhoDeCompras()
print(carrinho)

# criando produtos
prod_1 = Produto('Camiseta', 50)
prod_2 = Produto('Iphone', 15000)
prod_3 = Produto('Caneca', 15.90)

carrinho.inserir_produto(prod_1)
carrinho.inserir_produto(prod_2)
carrinho.inserir_produto(prod_1)
carrinho.inserir_produto(prod_3)

carrinho.lista_produto()
print(carrinho.soma_total())