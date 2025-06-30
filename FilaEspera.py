
class FilaEspera:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def adicionar(self, apto):
        if self.inicio is None:
            self.inicio = apto
        else:
            aux = self.inicio
            while aux.proximo:
                aux = aux.proximo
            aux.proximo = apto
        self.fim = apto
        print("Apartamento adicionado à fila!")
        self.imprimir()

    def atribuir_vaga(self, vaga):
        if self.inicio is None:
            print("Fila vazia!")
            return

        apto = self.inicio
        apto.vaga = vaga
        self.inicio = self.inicio.proximo
        if self.inicio is None:
            self.fim = None

        print(f"Apartamento {apto.numero} agora possui a vaga {vaga}.")

    def imprimir(self):
        print("Fila de espera por vaga: ")
        if self.inicio is None:
            print("Fila vazia.")
        else:
            aux = self.inicio
            while aux:
                print(aux)
                aux = aux.proximo