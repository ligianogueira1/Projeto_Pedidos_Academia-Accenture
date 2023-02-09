import lib
import csv_sistema
import uuid

nome_do_arquivo = "clientes.csv"

def localiza_cliente():
    lib.limpar_tela()
    lista = csv_sistema.ler(nome_do_arquivo)
    print("-" * 60)
    for idx, item in enumerate(lista):
        print("índice: " + str(idx + 1))
        print("Nome: " + item["nome"])
        print("Telefone: " + item["telefone"])
        print("E-mail: " + item["e-mail"])
        print("-" * 60)

    indice = input("Digite o índice do cliente o qual você deseja selecionar: \n")
    cliente = lista[int(indice) - 1]
    if cliente == None:
        lib.mensagem("Opção inválida.")
        localiza_cliente()

    return cliente


def cadastrar():
    lib.limpar_tela()

    cliente = {}
    cliente["id"] = str(uuid.uuid4())
    cliente["nome"] = input("Digite o nome do cliente: ")
    cliente["telefone"] = input("Digite o telefone do cliente: ")
    cliente["e-mail"] = input("Digite o e-mail do cliente: ")

    lista = csv_sistema.ler(nome_do_arquivo)
    lista.append(cliente)
    csv_sistema.salvar(lista, nome_do_arquivo)
    lib.mensagem("Cliente cadastrado com sucesso!")


def listar():
    lista = csv_sistema.ler(nome_do_arquivo)
    print("-" * 60)
    for item in lista:
        print("Nome: " + item["nome"])
        print("Telefone: " + item["telefone"])
        print("E-mail: " + item["e-mail"])
        print("-" * 60)
    lib.espera(5)
    lib.limpar_tela()

    input("Digite enter para continuar.")
    lib.limpar_tela()