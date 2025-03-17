# Exercício 3: Uso de Property
 
# Modifique a classe Lampada do Exercício 2 para usar o decorator property. Reescreva os getters e setters usando a sintaxe de property. Certifique-se de que a funcionalidade de ligar e desligar a lâmpada permaneça a mesma.

class Lampada:
    def __init__(self, estado):
        self.estado = estado

    @property    
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, estado):
        while(estado != 'ligado' and estado != 'desligado'):
            print(f' \'{estado}\' é um valor inválido, apenas os valores \'ligado\' e \'desligado\' serão aceitos.') 
            estado = input('Insira o valor novamente: ')
        self.__estado = estado

lamp1 = Lampada('desligado')
lamp1.estado = 'ligados'
print(lamp1.estado)