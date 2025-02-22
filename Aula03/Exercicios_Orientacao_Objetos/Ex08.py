# 8. Conta Bancária Simplificada 
# Descrição: Crie uma classe ContaBancaria com atributos para o titular da conta, número da conta e saldo. Inclua métodos para depositar e sacar dinheiro, além de um método para exibir as informações da conta.

class ContaBancaria:
    def __init__(self, titular, agencia, saldo):
        self.titular = titular
        self.agencia = agencia
        self.saldo = saldo

    def Depositar(self, quantia):
        if quantia <= 0:
            print(f'Quantia inválida.')
        else:
            self.saldo += quantia

    def Sacar(self, quantia):
        if quantia > self.saldo:
            print(f'Saldo insufíciente.')
        else:
            self.saldo -= quantia

    def MostrarDados(self):
        print(f'Informações Bancárias:\nNome do títula: {self.titular}\nNúmero da agência: {self.agencia}\nSaldo da conta: R$ {self.saldo}\n')
    
conta = ContaBancaria('Diogo', '101010-1', 50)
conta.MostrarDados()
conta.Depositar(1000000)
conta.MostrarDados()
conta.Sacar(100000000000000000)
conta.Sacar(1000)
conta.MostrarDados()