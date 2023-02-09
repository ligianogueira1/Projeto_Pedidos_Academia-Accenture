import lib
import cadastro_cliente
import cadastro_pedidos

print("-" * 60)
print("Bem vindo(a) ao Programa de Pedidos de Clientes!")
print("-" * 60)

while (True):
    print("Selecione uma das opções abaixo:\n")
    print("1 - Cadastro de cliente")
    print("2 - Lista de clientes")
    print("3 - Cadastro de pedidos")
    print("4 - Lista de pedidos")
    print("5 - Sair")

    opcao = int(input())

    if opcao == 1:
        cadastro_cliente.cadastrar()
    elif opcao == 2:
        cadastro_cliente.listar()
    elif opcao == 3:
        cadastro_pedidos.cadastrar()
    elif opcao == 4:
        cadastro_pedidos.listar()
    elif opcao == 5:
        break
    else:
        lib.mensagem("Opção inválida.")

    lib.limpar_tela()