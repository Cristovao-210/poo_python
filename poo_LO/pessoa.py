from datetime import datetime

class Pessoa:

    # VARIÁVEL DA CLASSE. 
    # TODOS OS MÉTODOS DA CLASSE TEM ACESSO A ELA
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    # construtor
    # atributos de instância
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo.')
            return
        print(f'{self.nome} está comendo {alimento}')
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return
        print(f'{self.nome} parou de comer.')
        self.comendo = False

    def falar(self, assunto):
        if self.comendo:
             print(f'{self.nome} não pode falar comendo.')
             return
        
        if self.falando:
             print(f'{self.nome} já está falando.')
             return
        
        print(f'{self.nome} está falando sobre {assunto}.')
        self.falando = True


    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando.')
            return
        print(f'{self.nome} parou de falar.')
        self.falando = False

    def get_ano_nascimento(self):
        # usando variável da classe
        return self.ano_atual - self.idade
    
    # Métodos de classe tem relação com o que é geral da classe. Não tem necessáriamente relação com a instância
    # devem ser utilizados de acordo com a responsabilidade... tem relação com a classe ou com a instância?

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento): # cls é a convenção para o equivalente ao self nos métodos de classe
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade) # aqui é como se estivesse chamando o construtor da classe
