#5. Registro de Alunos 
# Descrição: Crie uma classe Aluno com atributos para nome, matrícula e curso. Adicione métodos para mudar o curso do aluno e outro para exibir as informações do aluno.

class Aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
    
    def MudarCurso(self, novo_curso):
        print(f'Curso de {self.curso} alterado para {novo_curso}')
        self.curso = novo_curso
    
    def MostrarDados(self):
        print(f'Informações do aluno:\nNome: {self.nome}\nMatrícula: {self.matricula}\nCurso: {self.curso}\n')

aluno = Aluno('Diogo Antonny', '2044223', 'ADS' )
aluno.MostrarDados()
aluno.MudarCurso('ADM')
