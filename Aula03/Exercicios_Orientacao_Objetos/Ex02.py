# 2. Gerenciamento de Pessoas 
# Descrição: Crie uma classe Pessoa com atributos para nome, idade e endereço. Inclua métodos para alterar o endereço e outro para exibir todas as informações da pessoa.

class Pessoa:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def AlterarEndereco(self, novo_endereco):
        self.endereco = novo_endereco

    def ExibirDados(self):
        print(f'Informações da Pessoa:\nNome: {self.nome}\nIdade: {self.idade}\nEndereço: {self.endereco}\n')

pessoa = Pessoa('Diogo', '20', 'Acre 2.0')
pessoa.ExibirDados()
pessoa.AlterarEndereco('Acre 3.0')
pessoa.ExibirDados()