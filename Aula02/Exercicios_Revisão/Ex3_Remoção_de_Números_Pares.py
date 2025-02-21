'''Implemente uma função chamada remover_pares que receba uma lista de
números inteiros e retorne uma nova lista contendo apenas os números
ímpares. Utilize um loop for para percorrer a lista e verifique se cada
número é ímpar. Por fim, imprima a lista original e a lista resultante
com os números ímpares.'''

def remover_pares(lista_inteiros):
    numeros_impares = []
    for numero in lista_inteiros:
        if numero % 2 != 0:
            numeros_impares.append(numero)
    return numeros_impares

lista_inteiros = [1,2,3,4,5,6,7,8,9,10]
lista_impares = remover_pares(lista_inteiros)

print(f'Números Inteiros: {lista_inteiros}')
print(f'Números Impáres: {lista_impares}')