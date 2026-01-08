
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"A pessoa {self.nome} tem {self.idade} anos e está se apresentando.")


pessoa1 = Pessoa("Carlos", 35)
pessoa2 = Pessoa("Ana", 22)


pessoa1.apresentar()
pessoa2.apresentar()
