# 8. Gerar a sequência de Fibonacci até um número fornecido pelo usuário
# Use loops para gerar a sequência e estruturas condicionais para verificar o limite.

numero = int(input("Insira um número: "))
cont = 0
f2 = 1
f1 = f2 - 1

print(f1)
print(f2)

while cont <= numero:
    print(f1 + f2)
    temp = f2
    f2 += f1
    f1 = temp
    cont += 1
