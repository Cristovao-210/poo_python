'''
Relações entre classes:

Associação - Usa
Agregação - Tem
Composição - É dono
Herança - É (outro objeto)

'''
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeClasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeClasse} está falando...')

class Cliente(Pessoa): # Cliente herda de pessoa. Cliente é uma pessoa.
    def comprar(self):
        print(f'{self.nomeClasse} está comprando...')


class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nomeClasse} está estudando...')
    

pessoa1 = Pessoa('Tião', 18)
print(pessoa1.nome)
pessoa1.falar()
print()

cliente1 = Cliente('Pedro', 32)
print(cliente1.nome)
cliente1.comprar()
print()

aluno1 = Aluno('Barnabé', 95)
print(aluno1.nome)
aluno1.estudar()

