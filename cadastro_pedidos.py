import lib
import csv_sistema
import cadastro_cliente
import uuid

nome_do_arquivo = "pedidos.csv"
   
def cadastrar():
    lib.limpar_tela()

    cliente = cadastro_cliente.localiza_cliente()

    pedido = {}
    pedido["id"] = str(uuid.uuid4())
    pedido["cliente_id"] = cliente["id"]
    pedido["produto"] = input("Digite o nome do produto: \n")
    pedido["quantidade"] = input("Digite a quantidade: \n")
    pedido["valor"] = input("Digite o valor: \n")
    pedido["valor_total"] = float(pedido["quantidade"]) * float(pedido["valor"])

    lista = csv_sistema.ler(nome_do_arquivo)
    lista.append(pedido)
    csv_sistema.salvar(lista, nome_do_arquivo)
    lib.mensagem("Pedido cadastrado com sucesso!")


def listar():
    lib.limpar_tela()
    lista = csv_sistema.ler(nome_do_arquivo)
    print("-" * 60)
    for item in lista:
        print("Id: " + item["id"])
        cliente = csv_sistema.busca_por_id(item["cliente_id"], "clientes.csv")
        print("Cliente: " + cliente["nome"])
        print("Quantidade: " + item["quantidade"])
        print("Valor da unidade: R$" + item["valor"])
        print("Valor total: R$" + item["valor_total"])
        print("-" * 60)

    input("Digite enter para continuar.")
    lib.limpar_tela()