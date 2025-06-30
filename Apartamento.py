
class Apartamento:
    def __init__(self, id, numero, torre, vaga=None):
        self.id = id
        self.numero = numero
        self.vaga = vaga
        self.torre = torre
        self.proximo = None

    def cadastrar(self):
        self.id = int(input("ID: "))
        self.numero = input("Número: ")
        self.vaga = None
        print("Quais são os dados da torre? ")
        self.torre.cadastrar()

    def imprimir(self):
        print(f"Apartamento: {self.numero} | ID Apartamento: {self.id}")
        print(f"Torre: {self.torre}")
        print(f"Vaga {self.vaga if self.vaga is not None else "Sem vaga"}")

    def __str__(self):
        return (f"Apartamento: {self.numero} | Torre: {self.torre.nome} | "
                f"Vaga {self.vaga if self.vaga else "Esperando!"}")
