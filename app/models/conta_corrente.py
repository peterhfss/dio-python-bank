# Classe Modelo de Conta Corrente 

from models.conta import Conta
from models.saque import Saque

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao['tipo'] == Saque.__name__]
        )

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print('\n === Operação falhou! O valor do saque excede o limite. ===')
        elif excedeu_saques:
            print('\n=== Operação falhou! Número máximo de saques excedido. ===')
        else:
            return super().sacar(valor)
        
        return False
    
    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            CC:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """