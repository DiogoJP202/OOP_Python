# Exercício 4: Associação Simples 
# Crie uma classe Professor e uma classe Disciplina. Um professor pode estar associado a várias disciplinas, mas essa associação não implica em um relacionamento forte onde a existência da disciplina depende do professor. A relação deve ser uma associação simples. 
# • Defina a classe Disciplina com um atributo nome. 
# • Defina a classe Professor com um atributo nome e uma lista de Disciplinas. 
# • No exemplo de uso, crie algumas disciplinas e associe-as a um professor.

class Professor:
    def __init__(self, nome, disciplina = None):
        self.nome = nome
        self.disciplinas = []

    def adicionar_disciplinas(self, *disciplinas):
        self.disciplinas.extend(disciplinas)

class Disciplina:
    def __init__(self, nome):
        self.nome = nome

mat = Disciplina("Matemática")
geo = Disciplina("Geográfia")
por = Disciplina("Português")

professor = Professor("João")
professor.adicionar_disciplinas(mat, geo, por)