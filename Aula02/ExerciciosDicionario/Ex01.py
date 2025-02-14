# Preencha um dicionário com as informações de 5 produtos fornecidos pelo usuário.
# - Solicite os dados ao usuário
# - Utilize o nome do produto como chave e o preço como valor.
# - Percorra o dicionário e exiba o nome dos produtos com preço
# superior a R$ 50,00.

produtos = {}
for _ in range(5):
    nome = input('Insira o nome do produto: ')
    preco = float(input('Insira o valor do produto: '))
    produtos[nome] = preco

for item in produtos.items():
    if item[1] >= 50: 
        print(item)



