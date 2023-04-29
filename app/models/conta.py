# Classe Modelo de Conta

from models.historico import Historico

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = '0001'
        self._cliente = cliente
        self._historico = Historico()

    """
    Método da classe Conta para 
    criação de uma nova conta.
    """
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    

    """
    Decorator property para definir getters na classe Conta
    """
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    """
    Métodos saque e deposito da classe Conta 
    """
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print(f'\n*** Operação falhou! Saldo insuficiente! ***')

        elif valor > 0:
            self._saldo -= valor
            print(f'\n=== Saque no valor de R$ {valor} realizado com sucesso!====')
            return True
        else:
            print(f'\n*** Operação falhou! Valor inválido! ***')
        return False
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f'\n=== Depósito no valor de R$ {valor} realizado com sucesso! ===')
        else:
            print(f'\n*** Operação falhou! O valor informado é inválido. ***')
            return False
        
        return True