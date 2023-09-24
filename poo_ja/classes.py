# herança

#================================================================
class Funcionario(object):
	"""docstring for Funcionario"""
	def __init__(self, nome, salario, sobrenome):
		self.nome = nome
		self.sobrenome = sobrenome
		self.salario = salario

	def criar_nome_completo(self):
		return f'{self.nome} {self.sobrenome}'

#================================================================		

class Professor(Funcionario):
	cargo = "Professor"

#================================================================

class Tecnico_Adm(Funcionario):
	cargo = "Técnico-administrativo"

#================================================================

class Calculadora:

	# construtor
	def __init__(self, x_inicial, y_inicial):
		self.x = x_inicial
		self.y = y_inicial

	# retorna atributos	
	def retornaX(self):
		return self.x

	def retornaY(self):
		return self.y 

	# operações da calculadora	
	def soma(self):
		return self.x + self.y

	def subtrai(self):
		return self.x - self.y

	def multiplica(self):
		return self.x * self.y

	def divide(self):
		return self.x / self.y

