# 5. Calcular o fatorial de um número usando loop do-while (ou equivalente em Python)
numero = int(input('Digite um número: '))
cont = 1
soma = 1
while True:
    soma *= cont
    cont += 1
    if cont > numero:
        break
print(f'O valor fatorial é {soma}')