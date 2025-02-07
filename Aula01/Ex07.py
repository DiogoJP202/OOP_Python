# 7. Determinar se um número fornecido pelo usuário é primo
# Use loops e estruturas condicionais para fazer a verificação.
numero = int(input('Digite um número: '))
cont = 1
dividiveis = 0
while cont <= numero:
    if numero % cont == 0:
        dividiveis += 1
    cont += 1
if dividiveis > 2:
    print('Não é primo')
else:
    print('É primo')


