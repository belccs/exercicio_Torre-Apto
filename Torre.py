
class Torre:
    def __init__(self, id, nome, end):
        self.id = id
        self.nome = nome
        self.end = end

    def cadastrar(self):
        self.id = int(input("ID da Torre: "))
        self.nome = input("Nome: ")
        self.end = input("Endereço: ")

    def imprimir(self):
        print(f"Torre: {self.id} | Nome: {self.nome} | Endereço: {self.end}")

    def __str__(self):
        return f"Torre: {self.id} | Nome: {self.nome} | Endereço: {self.end}"
