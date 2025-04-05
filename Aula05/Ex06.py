# Exercício 6: Agregação 
# Crie uma classe Departamento e uma classe Funcionario. Um departamento pode ter vários funcionários, mas cada funcionário pode existir independentemente do departamento. A relação entre Departamento e Funcionario deve ser uma agregação. Defina a classe Funcionario com atributos nome e cargo. Defina a classe Departamento com um atributo para armazenar uma lista de Funcionarios. No exemplo de uso, crie um departamento e adicione alguns funcionários a ele.

class Departamento:
    def __init__(self):
        self.funcionarios = []

    def adicionarFuncionario(self, funcionario):
        if funcionario not in self.funcionarios:
            self.funcionarios.append(funcionario)
        else:
            print('Funcionário já está presente na lista.')

class Funcionario:
    def __init__(self, nome, cargo):
        self.nome = nome
        self.cargo = cargo

func1 = Funcionario("Diogo", "Desenvolvedor de software")
func2 = Funcionario("Alessandra", "Desenvolvedora de software")
depa1 = Departamento()
depa1.adicionarFuncionario(func1)
depa1.adicionarFuncionario(func2)