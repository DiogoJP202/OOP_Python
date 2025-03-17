# Exercício 4: Validação em Setter 

# Crie uma classe Pessoa com um atributo privado idade e um atributo público nome. Use um getter e um setter para idade, e adicione validação no setter para garantir que a idade não seja negativa. Se uma idade negativa for passada, defina a idade como 0 e imprima uma mensagem de aviso.

class Pessoa:
    def __init__(self, idade, nome):
        self.nome = nome
        self.idade = idade

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, nova_idade):
        if nova_idade < 18:
            self._idade = 0
            print('Idade inválida! Idade precisa ser maior que 17, idade definida para 0.')
        else:
            self._idade = nova_idade

pessoa1 = Pessoa(20, 'Diogo')
print(pessoa1.idade)
pessoa1.idade = 5
print(pessoa1.idade)