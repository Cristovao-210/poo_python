from classes import Calculadora

numX = int(input('Insira o primeiro valor da operação: '))
numY = int(input('Insira o segundo valor da operação: '))

fatores = Calculadora(numX, numY)

X = fatores.retornaX()
Y = fatores.retornaY()
valores = f'''
			Valor de X: {X}
			Valor de Y: {Y}
'''
print(valores)
print('X   |  Y')
operacoes = ['+', '-', '*', '/']
for sinal in operacoes:
	match sinal:
		case '+':
			resultado = fatores.soma()
			print(f'{X} {sinal} {Y} = {resultado}')
		case '-':
			resultado = fatores.subtrai()
			print(f'{X} {sinal} {Y} = {resultado}')
		case '*':
			resultado = fatores.multiplica()
			print(f'{X} {sinal} {Y} = {resultado}')
		case '/':
			resultado = fatores.divide()
			print(f'{X} {sinal} {Y} = {resultado}')