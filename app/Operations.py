# Operações bancárias PyBank
import textwrap

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
    
    print("Não foi realizada movimentações." if not extrato else extrato)
    print(f'Saldo : R$ {saldo:.2f}')
    print("==================================")

def novo_usuario(usuarios):
     cpf = input("Informe seu CPF (somente números):")
     usuario = buscar_usuario(cpf , usuarios)

     if usuario:
          print(" === CPF do usuário já esta cadastrado ===")
          return
     
     nome = input("Informe o nome completo: ")
     data_nascimento= input("Informe a data de nascimento (dd-mm-aaaa): ")
     endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/ sigla estado): ")

     usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco })

     print(" === Usuário cadastrado com sucesso! ===")
          
def buscar_usuario(cpf, usuarios):
     usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
     return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
     cpf = input("Informe o CPF do usuário: ")
     usuario = buscar_usuario(cpf, usuarios)

     if usuario:
          print(" === Conta criada com sucesso! === ")
          return ({"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario})
     
     print(" **** Usuário não encontrado. Operação cancelada! ****")

def listar_contas(contas):
     for conta in contas:
          linha = f"""
                Agência: \t{conta["agencia"]}
                C/C: \t{conta["numero_conta"]}
                Titular:\t{conta["usuario"]["nome"]}
          """    
          print("=" * 100)
          print(textwrap.dedent(linha))