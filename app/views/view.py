from views import viewCliente


def menu():
        menu = """

        ###### Sistema PyBank ######

        [d] Depositar
        [s] Sacar
        [e] Extrato
        [nu] Novo Usuário
        [nc] Nova Conta
        [lc] Listar Contas
        [q] Sair


        => """
        return input(menu)

def main():
    
    while True:

        opcao = menu()

        if opcao == 'd':
            viewCliente.depositar()
            
        elif opcao == "s":
            viewCliente.sacar()
             
        elif opcao == "e":
            viewCliente.exibir_extrato()
            
        elif opcao == "nu":
            viewCliente.criar_cliente()
            
        elif opcao == "nc":
            viewCliente.criar_conta()
        
        elif opcao == "lc":
            viewCliente.lista_contas()
           
        elif opcao == "q":
            print("Encerrando sessão no PyBank...")
            break
        else:
            print('Operação inválida! Favor selecionar novamente a operação desejada.')

def start():
    return main()