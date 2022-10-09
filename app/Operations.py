# Operações bancárias PyBank

saldo = 0
extrato = ""
limite = 500
total_saque = 0
LIMITE_SAQUE = 3

def depositar():

    global saldo, extrato

    print('Depósito\n')
    valor = float(input('Informe o valor desejado para depósito: '))
    if valor < 0:
        print(f'Favor informe um valor acima de 0')
    else:
        saldo += valor
        print(f'O novo saldo é R$ {saldo:.2f}')
        # adiciona a informação do depósito na variável extrato
        extrato += str(f'Depósito R$ {valor:.2f}\n') 

def sacar():

    global saldo , total_saque, extrato

    print("Saque\n")
    valor = float(input('Informe o valor desejado para o saque: '))

    if valor > saldo:
        print("Saldo insuficiente!")
    elif( total_saque < LIMITE_SAQUE):
        if(valor < 0):
            print("Operação falhou! Valor informado inválido.")
        elif (valor <= limite):
            saldo -= valor
            print(f"Saque no valor de R$ {valor:.2f} realizado com sucesso!")
            total_saque+= 1
            extrato += str(f'Saque R$ {valor:.2f}\n')
        else:
            print(f"Operação falhou! Limite do saque até {limite:.2f}")
    else:
        print("Quantidade total de saques diários atingido!")

def realizar_extrato():
    
    print("\n============= Extrato ============\n")
    # 
    print("Não foi realizada movimentações." if not extrato else extrato)
    print(f'Saldo : R$ {saldo:.2f}')
    print("==================================")

        