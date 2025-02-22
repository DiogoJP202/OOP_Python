# 3. Sistema de Biblioteca 
# Descrição: Desenvolva uma classe Livro com atributos para título, autor, ano de publicação e disponibilidade. Adicione métodos para emprestar e devolver o livro, alterando seu status de disponibilidade.

class Livro:
    def __init__(self, titulo, autor, anoPublicacao):
        self.titulo = titulo
        self.autor = autor
        self.anoPublicacao = anoPublicacao
        self.disponibilidade = True
    
    def EmprestarLivro(self):
        if self.disponibilidade:
            self.disponibilidade = False
            print('Livro emprestado com sucesso!')
        else: 
            print('Livro indisponível.')
    
    def DevolverLivro(self):
        if self.disponibilidade:
            print('Livro já foi devolvido.')
        else:
            self.disponibilidade = True
            print('Livro devolvido com sucesso!')

    def ExibirDados(self):
        print(f'Dados do livro:\nTítulo: {self.titulo}\nAutor: {self.autor}\nAno de publicação: {self.anoPublicacao}\nStatus: {"Livro disponível." if self.disponibilidade else "Livro indisponível."}\n')

livro = Livro('Senhor dos Anéis', 'J. R. R. Tolkien', '1954')
livro.DevolverLivro()
livro.EmprestarLivro()
livro.ExibirDados()
livro.DevolverLivro()
livro.ExibirDados()