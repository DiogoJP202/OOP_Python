class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.set_idade(idade)
        
    def set_idade(self, nova_idade):
        while(nova_idade < 18):
            nova_idade = int(input(f'Insira uma idade maior que 17: '))
        self.idade = nova_idade
        
class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.set_salario(salario)
        
    def set_salario(self, novo_salario):
        self.__salario = novo_salario
        
    def get_salario(self):
        return self.__salario
        
    def calcular_salario_anual(self):
        return self.get_salario() * 12
        
class Departamento:
    def __init__(self):
        self.listaFuncionarios = []
    
    def adicionar_funcionario(self, *funcionarios):
        self.listaFuncionarios.extend(funcionarios)
    
    def calcular_total_salarios(self):
        total = 0
        for funcionario in self.listaFuncionarios:
            total += funcionario.calcular_salario_anual()
        return total
        
    def listar_funcionarios(self):
        print('Listando funcionários:')
        for funcionario in self.listaFuncionarios:
            print(f'Nome: {funcionario.nome} \nSalário anual: {funcionario.calcular_salario_anual()}')
            
funcionario1 = Funcionario('Alberto', 44, 7000)
funcionario2 = Funcionario('Maria', 22, 4000)
funcionario3 = Funcionario('Alex', 13, 2400)

departamento1 = Departamento()
departamento1.adicionar_funcionario(funcionario1, funcionario2, funcionario3)
departamento1.listar_funcionarios()

print(f'Gasto total com salários anualmente: {departamento1.calcular_total_salarios()}')
