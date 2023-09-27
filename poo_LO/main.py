from associacao import Escritor, Caneta, MaquinaDeEscrever

print("Classes sendo utilizadas de forma independente: ")
escritor_1 = Escritor("Fernando Pessoa")
caneta_1 = Caneta("Bic")
maquina_1 = MaquinaDeEscrever()
print(f'{escritor_1.nome} usa canetas {caneta_1.marca} para escrever')
maquina_1.escrever()

# Utilizando associação
print("\nClasses sendo utilizadas com associação:\n ")
# O atributo ferramenta da classe escritor pode receber um objeto(instância) 'INTEIRA' tanto das classes Caneta como MaquinaDeEscrever
escritor_1.ferramenta = maquina_1
escritor_1.ferramenta.escrever()
print()
escritor_1.ferramenta = caneta_1
escritor_1.ferramenta.escrever()