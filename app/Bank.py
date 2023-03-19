from Operations import *

# Menu de navegação do PyBank

def menu():
    menu = """

    ### Sistema PyBank ###

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nu] Novo Usuário
    [nc] Nova Conta
    [lc] Listar Contas
    [q] Sair do Sistema


    => """
    return input(menu)

def main():

    # Constantes
    LIMITE_SAQUE = 3
    AGENCIA = "0001"

    # Dados 
    saldo = 0
    extrato = ""
    limite = 500
    total_saque = 0
    usuarios = []
    contas = []

    while True:

        opcao = menu()

        if opcao == 'd':
            valor = float(input('Informe o valor desejado para depósito: '))
            
            saldo, extrato = depositar(saldo, valor, extrato)
            
        elif opcao == "s":
            valor = float(input('Informe o valor desejado para saque: '))

            saldo, extrato = sacar(
                saldo = saldo,
                valor =valor,
                extrato = extrato,
                limite = limite,
                total_saque = total_saque,
                limite_saque =LIMITE_SAQUE,    
            )
        elif opcao == "e":
            realizar_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            novo_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA , numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            print("Encerrando sessão no PyBank...")
            break
        else:
            print('Operação inválida! Favor selecionar novamente a operação desejada.')

main()