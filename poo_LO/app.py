from pessoa import Pessoa

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

'''
# exemplo com método de classe

# p1 = Pessoa('Heitor', 11)

p1 = Pessoa.por_ano_nascimento('Heitor', 2012)
print(p1.idade)
print(p1.get_ano_nascimento())
