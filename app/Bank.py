from Operations import *

# Menu de navegação do PyBank

menu = """

### Sistema PyBank ###

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair do Sistema


 => """

    
while True:

    opcao = input(menu)

    if opcao == 'd':
        depositar()
        
    elif opcao == "s":
        sacar()

    elif opcao == "e":
        realizar_extrato()

    elif opcao == "q":
        print("Encerrando sessão no PyBank...")
        break
    else:
        print('Operação inválida! Favor selecionar novamente a operação desejada.')


