
from Torre import Torre
from Apartamento import Apartamento
from FilaEspera import FilaEspera

fila = FilaEspera()

def menu():
    while True:
        print("\n --- MENU ---")
        menu = "\n1. Adicionar apartamento na fila de espera"\
               "\n2. Atribuir vaga para o próximo apartamento"\
               "\n3. Mostrar fila de espera"\
               "\n4. Sair"
        print(menu)
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("Dados do Apartamento: ")
            id_apto = int(input("ID do apartamento: "))
            numero_apto = input("Número do apartamento: ")
            print("Dados da Torre: ")
            id_torre = int(input("ID da torre: "))
            nome_torre = input("Nome da torre: ")
            endereco_torre = input("Endereço da torre: ")
            torre = Torre(id_torre, nome_torre, endereco_torre)
            apto = Apartamento(id_apto, numero_apto, torre)
            fila.adicionar(apto)

        if opcao == "2":
            vaga = int(input("Digite o numero da vaga a ser atribuída: "))
            fila.atribuir_vaga(vaga)

        if opcao == "3":
            fila.imprimir()

        elif opcao == "4":
            print("Sair, sistema encerrado")
            break

        else:
            print("Opção inválida.")

menu()