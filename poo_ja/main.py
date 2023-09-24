from classes import Professor, Tecnico_Adm

lista_funcionarios = [

	Professor("Márcio", 8000, "Rosa"),
	Tecnico_Adm("Cristóvão", 18000, "Silva"),
	Tecnico_Adm("Heitor", 10000, "Dias da Rosa")

]

for f in lista_funcionarios:
	print("=" * 30)
	print(f' Nome: {f.criar_nome_completo()}\n Cargo:{f.cargo}\n Salário: {f.salario}')

print("=" * 30)