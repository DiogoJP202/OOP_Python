class Funcionario:
    def __init__(self, nome, data_nasc, sexo, salario, endereco):
        self.nome = nome
        self.data_nasc = data_nasc
        self.sexo = sexo
        self.salario = salario
        self.endereco = endereco

    def exibir_dados(self):
        print(f'Informações do funcionário:\nNome: {self.nome}\nData de nascimento: {self.data_nasc}\nSexo: {self.sexo}\nSalário: {self.salario}\n')
        self.endereco.exibir_dados()

class Endereco:
    def __init__(self, rua, numero, bairro, complemento, cep):
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.complemento = complemento
        self.cep = cep

    def exibir_dados(self):
        print(f'Informações do Endereço:\nRua: {self.rua}\nNúmero: {self.numero}\nBairro: {self.bairro}\nComplemento: {self.complemento}\nCep: {self.cep}')

endereco = Endereco('Joäo matos', 303, 'Vila Formosa', 'apt40', '0331-000')
funcionario = Funcionario('Antonio', "10/01/1998", 'Masculino', 3999.00, endereco)
funcionario.exibir_dados()