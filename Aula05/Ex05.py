# Exercício 5: Dependência 
# Crie uma classe Mensagem e uma classe Correio. A classe Correio deve ter um método que envia uma Mensagem. A relação entre Correio e Mensagem deve ser uma dependência. 
# • Defina a classe Mensagem com um atributo texto. 
# • Defina a classe Correio com um método enviar que aceita um objeto Mensagem como parâmetro e imprime o texto da mensagem. 
# • No exemplo de uso, crie uma mensagem e use o correio para enviá-la.

class Mensagem:
    def __init__(self, texto):
        self.texto = texto
        
class Correio:
    def __init__(self, mensagem):
        self.mensagem = mensagem

    def enviar(self):
        print(self.mensagem.texto)

mensagem = Mensagem("Hello, world!")
correio = Correio(mensagem)
correio.enviar()