"""
No encapsulamento clássico existem modificadores de acesso:

Public -> Pode ser acessado de fora da classe.
Protected -> Só pode ser acessado pelas 'classes herdeiras' e dentro da classe
Private -> só pode ser acessado de dentro da classe

No Python se usa por convenção:

_nomeVariavel -> Parcialmente privado. Não mostra na lista após o '.', mas é possível acessar. Equivalente ao PROTECTED
 A convenção é que essa variável seja utilizada apenas dentro da classe.

__nomeVariavel -> Totalmente privado. Indica que esse atributo não pode ser sobrescrito de forma alguma.
É o PRIVATE.
Quando utilizado, caso seja criada uma variável/atributo de mesmo nome, será considerada uma variável local da instância.
para acessar o valor desse atributo é necessário utilizar: 'nomeInstancia._nomeClasse__nomeAtributo ou método'.
Mas o mais recomendado é utilizar um GETTER sem SETTER para restringir o acesso direto.

os modificadores _ e __ se aplicam tanto a atributos quanto aos métodos.

"""

class BaseDeDados:
    def __init__(self):
        self.__dados = {}

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print("=" * 25)
            print(f'COD: {id}\nNOME: {nome}')
        print("=" * 25)

    def apaga_clientes(self, id):
        del self.__dados['clientes'][id]


bd = BaseDeDados()
bd.inserir_cliente(1, 'Pedro Drosa')
bd.inserir_cliente(2, 'Cristóvão Colombo')
bd.inserir_cliente(3, 'Ernesto Silva')
bd.inserir_cliente(4, 'Rosa da Rosa')

bd.lista_clientes()

print("\nProcessando Alterações...\n")
bd.inserir_cliente(4, 'Rosa da Costa')
bd.apaga_clientes(3)
bd.lista_clientes()

# criar outro atributo
bd.__dados = "Atributo da instãncia"
# para ver o atributo criado
print(bd.__dados)

# para ver o atributo real da classe
print("Atributo real: ", bd._BaseDeDados__dados)