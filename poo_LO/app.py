from pessoa import Pessoa
from produto import Produto

'''
# exemplos com métodos e atributos de instância

pessoa1 = Pessoa('Márcio', 42)
pessoa1.falar('Futebol')
pessoa1.comer('MANDIOCA')
pessoa1.parar_comer()
pessoa1.comer('PÊRA')
pessoa1.falar('política')
pessoa1.parar_comer()
pessoa1.parar_falar()
pessoa1.falar('política')

# usa um atributo de classe
print(pessoa1.get_ano_nascimento())

# exemplo com método de classe

# p1 = Pessoa('Heitor', 11)

p1 = Pessoa.por_ano_nascimento('Heitor', 2012)
print(p1.idade)
print(p1.get_ano_nascimento())

# exemplo de uso de método estático
print(p1.gerar_id())
print(Pessoa.gerar_id())

'''

### CLASSE PRODUTO ###

prod_1 = Produto("CAMISETA", 50)
prod_1.desconto(10)
print(f'{prod_1.nome}: {prod_1.preco}')

prod_2 =  Produto("CANECA", 'R$15')
prod_2.desconto(10)
print(f'{prod_2.nome}: {prod_2.preco}')