class Medico:
    def __init__(self, nome, idade, especialidade, *pacientes):
        self.nome = nome
        self.idade = idade
        self.especialidade = especialidade
        self.lista_pacientes = []
        self.lista_pacientes.extend(pacientes)

    def exibir_pascientes(self):
        cont = 1
        for paciente in self.lista_pacientes:
            print(f'Paciente {cont}: {paciente.nome}')
            cont += 1
        
    def media_idade_pacientes(self):
        mediaIdades = 0
        for paciente in self.lista_pacientes:
            mediaIdades += paciente.idade
        return mediaIdades / len(self.lista_pacientes)
    
class Paciente:
    def __init__(self, nome, idade):
        self.nome = nome 
        self.idade = idade

medico = Medico("Joäo", 30, "pediatra", Paciente("Cleber", 19), Paciente("Pedro", 23), Paciente("Maria", 35))
medico.exibir_pascientes()
print(f'{medico.media_idade_pacientes():.2f}')