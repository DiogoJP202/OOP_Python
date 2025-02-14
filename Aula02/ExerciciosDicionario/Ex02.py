# Preencha um dicionário com os dados de 5 alunos fornecidos pelo usuário.
# - Solicite os dados do usuário
# - Utilize o ra do aluno como chave e uma lista de três notas como valor.
# - Percorra o dicionário e exiba a média de cada aluno.

alunos = {}
for _ in range(5):
    RA = input('Insira o seu RA: ')
    nota1 = float(input('Insira a sua primeira nota: '))
    nota2 = float(input('Insira a sua segunda nota: '))
    nota3 = float(input('Insira a sua terceira nota: '))
    alunos[RA] = (nota1 , nota2 , nota3)
 
for aluno in alunos.items():
    media = ((aluno[1][0] + aluno[1][1] + aluno[1][2]) / 3)
    print(f"{aluno[0]} - {media}")
        