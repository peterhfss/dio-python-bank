# Operações bancárias PyBank



def depositar(saldo,valor,extrato, /):

    print('Depósito\n')
    
    if valor > 0:
        saldo += valor
        extrato += str(f'Depósito R$ {valor:.2f}\n') 
        print(f'Depósito realizado com sucesso! O novo saldo é de {saldo:.2f}')
    else:
        print("== Falha na Operação! Valor informado inválido. ==")
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, total_saque, limite_saque):

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = total_saque >= limite_saque

    if excedeu_saldo:
        print(" == Falha na operação! Vocë não possui saldo suficiente. ==")
    elif excedeu_limite:
        print(" == Falha na operação! O valor do saque excede o limite. ==")
    elif excedeu_saques:
        print(" == Falha na operação! Número total de saques excedido. ==")
    elif valor > 0:
            saldo -= valor
            print(f"Saque no valor de R$ {valor:.2f} realizado com sucesso!")
            total_saque+= 1
            extrato += str(f'Saque R$ {valor:.2f}\n')
    else:
         print(" == Falha na operação! Valor informado inválido. ==")

    return saldo, extrato

def realizar_extrato(saldo, /, *, extrato):
    
    print("\n============= Extrato ============\n")
    # 
    print("Não foi realizada movimentações." if not extrato else extrato)
    print(f'Saldo : R$ {saldo:.2f}')
    print("==================================")
