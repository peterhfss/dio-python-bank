"""
    Controller da entidade Cliente.
"""

from models.cliente import Cliente
from models.conta import Conta
from typing import List

class ClienteController:

    clientes = []
    contas =[]

    @classmethod
    def salvar_cliente(cls, cliente:Cliente) -> None:
        cls.clientes.append(cliente)
    
    @classmethod
    def filtrar_cliente(cls, cpf) -> Cliente:
        clientes_filtrados = [cliente for cliente in cls.clientes if cliente.cpf == cpf]
        return clientes_filtrados[0] if clientes_filtrados else None
    
    @classmethod
    def recuperar_conta_cliente(cls, cliente:Cliente) -> Cliente:
        if not cliente.contas:
            print('\n*** Cliente não possui conta! ***')
            return 
        
        return cliente.contas[0]
    
    @classmethod
    def salvar_conta(cls, cliente:Cliente,conta) -> None:
        cliente.contas.append(conta)
    
    @classmethod
    def listar_contas(cls, cliente:Cliente) -> List[Conta]:
        if cls.filtrar_cliente() != None:
            return cliente.contas
    