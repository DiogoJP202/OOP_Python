# Exercício 1: Básico de Membros Públicos e Privados 

# Crie uma classe ContaBancaria que tenha um atributo privado saldo e um atributo público titular. Inicialize ambos os atributos no método __init__. Em seguida, crie um método para depositar dinheiro e outro para exibir o saldo, garantindo que o saldo não possa ser acessado diretamente de fora da classe.

class ContaBancaria:
    def __init__(self, saldo, titula):
        self.titula = titula
        self.__saldo = saldo
    
    def depositarDinheiro(self, valor):
        self.__saldo += valor
        print(f'R${valor:.2f} depositado com sucesso! Valor atual: R${self.__saldo:.2f}')

    def exibirSaldo(self):
        print(f'R${self.__saldo:.2f}')
        
conta1 = ContaBancaria(500, "Fernando")
conta1.depositarDinheiro(150)
conta1.exibirSaldo()