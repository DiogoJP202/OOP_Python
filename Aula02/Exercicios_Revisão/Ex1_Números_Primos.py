'''Crie um programa que encontre e imprima os 20 primeiros números primos.
Um número é considerado primo se ele é maior que 1 e possui exatamente
dois divisores: 1 e ele mesmo. Utilize um loop while para iterar até
encontrar 20 números primos e um loop for para contar a quantidade de
divisores de cada número.'''

def verificarNumeroPrimo(n):
    divisores = 0
    for i in range(n+1):
        if n % i == 0:
            divisores += 1
        if divisores > 2:
            return False
    return True

qtdPrimos = 0
contador = 1
while qtdPrimos < 20:
    if verificarNumeroPrimo(contador) == True:
        print(contador)     
        qtdPrimos += 1
    contador += 1   