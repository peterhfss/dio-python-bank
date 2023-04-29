from controllers.cliente_controller import ClienteController
from models.pessoa_fisica import PessoaFisica
from models.conta_corrente import ContaCorrente
from models.deposito import Deposito
from models.saque import Saque


def criar_cliente():
    cpf = input('Informe o CPF (somente números):')
    if (ClienteController.filtrar_cliente(cpf) == None):
        nome = input('Informe o nome completo: ')
        data_nascimento = input('Informe a data de nascimento ( dd-mm-aaaa): ')
        endereco = input('Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ')

        cliente = (PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco))

        ClienteController.clientes.append(cliente)

        print('\n === Cliente criado com sucesso! ===')
    else:
        print('\n @@@ Cliente já possui cadastro! @@@')

def criar_conta():

    numero_conta = len(ClienteController.contas) + 1
    cpf = input('Informe o CPF (somente números):')
    cliente = ClienteController.filtrar_cliente(cpf)
    if ( cliente == None):
        if not cliente:
            print('\n @@@ Cliente não encontrado, encerrando fluxo de criação da conta! @@@')
            return
    conta = ContaCorrente.nova_conta(cliente, numero=numero_conta)
    ClienteController.contas.append(conta)
    cliente.contas.append(conta)

    print("\n=== Conta criada com sucesso! ===")

def lista_contas():
    for conta in ClienteController.contas:
        print('=' * 100)
        print(conta)

def depositar():
    cpf = input('Informe o CPF do cliente: ')
    cliente = ClienteController.filtrar_cliente(cpf)

    if not cliente:
        print('\n @@@ Cliente não encontrado! @@@ ')
        return
    
    valor = float(input('Informe o valor do depósito: '))
    transacao = Deposito(valor)

    conta = ClienteController.recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)

def exibir_extrato():
    cpf = input('Informe o CPF do cliente: ')
    cliente = ClienteController.filtrar_cliente(cpf)

    if not cliente:
        print('\n @@@ Cliente não encontrado! @@@ ')
        return 
    
    conta = ClienteController.recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    print('\n ======== EXTRATO ========')
    transacoes = conta.historico.transacoes

    extrato = ''
    if not transacoes:
        extrato = 'Não foram realizadas movimentações.'
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\n R$ {transacao['valor']: .2f}"

    print(extrato)
    print(f'\nSaldo: \n R$ {conta.saldo:.2f}')
    print('================================')

def sacar():
     cpf = input('Informe o CPF do cliente: ')
     cliente = ClienteController.filtrar_cliente(cpf)

     if not cliente:
        print('\n @@@ Cliente não encontrado! @@@ ')
        return 
     
     valor = float(input('Informe o valor do saque: '))
     transacao = Saque(valor)

     conta = ClienteController.recuperar_conta_cliente(cliente)
     if not conta:
         return
     
     cliente.realizar_transacao(conta, transacao)
    



