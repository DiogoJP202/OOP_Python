#1. Controle de Estoque
# Descrição: Implemente uma classe Produto com atributos para nome, preço e quantidade em estoque. Adicione métodos para adicionar e remover produtos do estoque, e um método para imprimir as informações

class Produto:
    def __init__(self, nome, preco, qtdEstoque):
        self.nome = nome
        self.preco = preco
        self.qtdEstoque = qtdEstoque
    
    def Adicionar(self, qtd):
        if qtd <= 0:
            print('Valor inválido! O quantidade miníma é de 1.')
        else:
            self.qtdEstoque += qtd

    def Remover(self, qtd):
        if qtd > self.qtdEstoque:
            print('Quantidade de estoque insuficiente.')
        else:
            self.qtdEstoque -= qtd

    def ExibirDados(self):
        print(f'Informações do produto:\nNome: {self.nome}\nPreço: ${self.preco}\nQuantidade no estoque: {self.qtdEstoque}\n')

produto = Produto('Apple', 0.07, 10)
produto.ExibirDados()
produto.Adicionar(5)
produto.Remover(20)
produto.Remover(1)
produto.ExibirDados()