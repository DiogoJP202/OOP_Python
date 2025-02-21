'''Desenvolva uma função chamada calcular_medias que receba uma lista de
listas, onde cada sublista contém três notas de um aluno. A função deve
calcular a média ponderada de cada aluno, considerando pesos de 30%
para as duas primeiras notas e 40% para a terceira nota.
Retorne uma lista com as médias calculadas e imprima as notas dos alunos
junto com as respectivas médias.'''

def calcular_medias(lista):
    medias = []
    for notas in lista:
        media = (notas[0] * 3 + notas[1] * 3 + notas[2] * 4) / 10
        medias.append(media)
    return medias

notas = [[10, 10, 10], [6, 8, 7]]
medias = calcular_medias(notas)
contador = 0

print('[======================]')
while contador < len(notas):
    print(f'Aluno {contador}: \nNota 1: {notas[contador][0]}\nNota 2: {notas[contador][1]}\nNota 3: {notas[contador][2]}\nMédia Ponderada: {medias[contador]}')
    contador += 1
    print('[======================]')