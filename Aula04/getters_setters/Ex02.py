# Exercício 2: Getters e Setters Simples 

# Crie uma classe Lampada com um atributo privado estado (ligado/desligado). Implemente métodos getters e setters para o atributo estado. O setter deve aceitar apenas os valores "ligado" ou "desligado" e alterar o estado da lâmpada de acordo.

class Lampada:
    def __init__(self, estado):
        self.set_estado(estado)

    def set_estado(self, estado):
        while(estado != 'ligado' and estado != 'desligado'):
            print(f' \'{estado}\' é um valor inválido, apenas os valores \'ligado\' e \'desligado\' serão aceitos.') 
            estado = input('Insira o valor novamente: ')
        self.__estado = estado
    
    def get_estado(self):
        return self.__estado

lamp1 = Lampada('desligado')
lamp1.set_estado('ligados')
print(lamp1.get_estado())