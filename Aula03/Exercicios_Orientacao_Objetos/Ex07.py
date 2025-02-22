# 7. Agendamento de Eventos 
# Descrição: Implemente uma classe Evento com atributos para nome do evento, data e número de participantes. Adicione métodos para alterar a data do evento e outro para exibir as informações do evento.

class Evento:
    def __init__(self, nome, data, numeroParticipantes):
        self.nome = nome
        self.data = data
        self.numeroParticipantes = numeroParticipantes
    
    def AlterarData(self, nova_data):
        self.data = nova_data

    def MostrarDados(self):
        print(f'Informações do evento:\nNome: {self.nome}\nData: {self.data}\nNumero de participantes: {self.numeroParticipantes}\n')

evento = Evento('Sla Summit', '10/02/2026', 1000)
evento.MostrarDados()
evento.AlterarData('10/03/2026')