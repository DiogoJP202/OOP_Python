# 8. Gerar a sequência de Fibonacci até um número fornecido pelo usuário
# Use loops para gerar a sequência e estruturas condicionais para verificar o limite.

numero = int(input("Insira um número: "))
cont = 1
soma = 0
while cont <= numero:
    soma += cont
    cont += 1
print(soma) 