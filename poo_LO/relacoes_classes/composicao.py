"""
Outro tipo de associação:

COMPOSIÇÃO -> Uma Classe é 'dona' de objetos de outra classe. Quando uma classe 'pertence' a outra classe.
Se a classe principal for apagada, todos os objetos gerados por ela serão apagados também.

"""

class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = [] # vai receber elemenos de uma classe específica para criar endereços.

    def insere_endereco(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado))

    def lista_endereco(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)


class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado

cliente1 = Cliente('Luiz', 32)
cliente1.insere_endereco('Patrocínio', 'MG')
print(cliente1.nome)
cliente1.lista_endereco()
print()

cliente2 = Cliente('Maria', 55)
cliente2.insere_endereco('Formosa', 'GO')
cliente2.insere_endereco('Formoso', 'MG')
print(cliente2.nome)
cliente2.lista_endereco()
print()

cliente3 = Cliente('João', 19)
cliente3.insere_endereco('Imperatriz', 'MA')
print(cliente3.nome)
cliente3.lista_endereco()
























