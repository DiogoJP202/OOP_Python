# Exercício 7: Herança + Agregação 

# Escreva um programa para armazenar dados de veículos. Crie a classe Motor que contém cilindrada e potencia. Crie a classe Veiculo contendo ano de fabricação, preco e motor. Crie a classe Carro, que herda da classe Veiculo e adiciona os atributos cor e modelo. Crie também o método exibir_dados para mostrar os dados do Carro. Crie a classe Caminhao, que herda da classe Veiculo e adiciona o atributos comprimento (em metros). Crie também o método exibir_dados para mostrar os dados do Caminhao. 

# Obs.: A classe Motor não possui relação de herança com a classe Veiculo, possui apenas uma relação de agregação (o veiculo possui um motor)

class Motor:
    def __init__(self, cilindrada, potencia):
        self.cilindrada = cilindrada
        self.potencia = potencia

    def exibir_dados(self):
        print(f"Informações do Moto:\nCilindradas: {self.cilindrada};\nPotência: {self.potencia};\n")

class Veiculo:
    def __init__(self, anoFabricacao, preco, motor):
        self.anoFabricacao = anoFabricacao
        self.preco = preco
        self.motor = motor

class Carro(Veiculo):
    def __init__(self, anoFabricacao, preco, motor, cor, modelo):
        super().__init__(anoFabricacao, preco, motor)
        self.cor = cor 
        self.modelo = modelo

    def exibir_dados(self):
        print(f"Informações do carro:\nAno fabricação: {self.anoFabricacao};\nPreço: {self.preco:.2f};\nCor: {self.cor};\nModelo: {self.modelo};")
        self.motor.exibir_dados()

class Caminhao(Veiculo):
    def __init__(self, anoFabricacao, preco, motor, comprimento):
        super().__init__(anoFabricacao, preco, motor)
        self.comprimento = comprimento

    def exibir_dados(self):
        print(f"Informações do caminhão:\nAno fabricação: {self.anoFabricacao};\nPreço: {self.preco:.2f};\nComprimento: {self.comprimento};")
        self.motor.exibir_dados()

motor1 = Motor(1000, 500)
motor2 = Motor(8000, 900)
carro = Carro(2010, 20000, motor1, "branca", "gol")
caminhao = Caminhao(2015, 80000, motor2, 10)
carro.exibir_dados()
# imprime os valores de todos os atributos do carro
caminhao.exibir_dados()
# imprime os valores de todos os atributos do caminhão