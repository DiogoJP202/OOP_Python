# 6. Controle de Animais de Estimação 
# Descrição: Desenvolva uma classe AnimalDeEstimacao com atributos para nome, espécie e idade. Inclua métodos para alterar a idade do animal e outro para exibir as informações do animal.

class AnimalDeEstimacao:
    def __init__(self, nome, especie, idade):
        self.nome = nome
        self.especie = especie
        self.idade = idade

    def AlterarIdade(self, nova_idade):
        if nova_idade <= 0:
            print('Adicione um número válido e acima de 0.')
        else:
            self.idade = nova_idade

    def MostrarDados(self):
        print(f'Informações do animal de estimação:\nNome: {self.nome}\nEspécie: {self.especie}\nIdade: {self.idade}\n')

pet = AnimalDeEstimacao('Shelby', 'Felino', 7)
pet.MostrarDados()
pet.AlterarIdade(-1)
pet.AlterarIdade(10)
pet.MostrarDados()