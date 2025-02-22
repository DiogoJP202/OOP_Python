# 4. Veículo 
# Descrição: Implemente uma classe Carro com atributos para marca, modelo, ano e quilometragem. Inclua métodos para dirigir o carro, que aumenta a quilometragem, e outro método para exibir informações do carro.

class Carro:
    def __init__(self, marca, modelo, quilometragem):
        self.marca = marca
        self.modelo = modelo
        self.quilometragem = quilometragem

    def Dirigir(self):
        print('Você está dirigindo o carro. Quilometragem aumetou para 1km.')
        self.quilometragem += 1

    def AumentarQuilometragem(self, quilometragem)
        if quilometragem <= 0:
            print('Insira um número válido acima de 0.')
        else:
            self.quilometragem += quilometragem

    def MostrarDados(self):
        print(f'Informações do carro:\nMarca: {self.marca}\nModelo: {self.modelo}\Quilometragem: {self.quilometragem}km\n')

carro = Carro('Fusquinha', '2.0', 0)
carro.MostrarDados()
carro.Dirigir()
carro.AumentarQuilometragem(-1)
carro.AumentarQuilometragem(10)
carro.MostrarDados()