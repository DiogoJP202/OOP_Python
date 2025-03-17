# Exercício 5: Property Avançada 

# Crie uma classe Circulo com um atributo privado raio. Use a propriedade property para criar getters e setters para o raio. Além disso, adicione um método de propriedade area que calcule e retorne a área do círculo (área = π * raio^2). Garanta que o raio não possa ser negativo.
import math

class Circulo:
    def __init__(self, raio):
        self.raio = raio
    
    @property
    def raio(self):
        return self._raio

    @raio.setter
    def raio(self, novo_raio):
        while(novo_raio < 0):
            novo_raio = float(input('O valor do raio não pode ser negativo. Insira o valor novamente: '))
        self._raio = novo_raio

    def calcularArea(self):
        return math.pi * (self._raio ** 2)

circulo1 = Circulo(-5)
print(circulo1.raio)
print(f'{circulo1.calcularArea():.2f}')