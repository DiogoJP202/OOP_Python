# Exercício 8: Composição 
# Crie uma classe Sala e uma classe Edificio. Um edifício deve conter várias salas, e a existência das salas deve depender da existência do edifício. Se o edifício for destruído, suas salas também serão. Defina a classe Sala com um atributo numero. Defina a classe Edificio com um atributo para armazenar uma lista de Salas. No construtor do Edificio, crie as Salas internamente. No exemplo de uso, crie um edifício e observe que as salas são criadas como parte do edifício.

class Sala:
    def __init__(self, numero):
        self.numero = numero


class Edificio:
    def __init__(self, *salas):
        self.listaDeSalas = []
        self.listaDeSalas.extend(salas)

    def adicionarSalas(self, sala):
        if sala not in self.listaDeSalas:
            self.listaDeSalas.append(sala)
        else:
            print("A sala já está presente na lista.")

edificio = Edificio(Sala(1), Sala(2), Sala(3), Sala(4))