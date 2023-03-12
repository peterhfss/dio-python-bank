from Operations import *

# Menu de navegação do PyBank

def menu():
    menu = """

    ### Sistema PyBank ###

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair do Sistema


    => """
    return input(menu)

def main():

    # Constantes
    LIMITE_SAQUE = 3

    saldo = 0
    extrato = ""
    limite = 500
    total_saque = 0

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

        elif opcao == "q":
            print("Encerrando sessão no PyBank...")
            break
        else:
            print('Operação inválida! Favor selecionar novamente a operação desejada.')

main()