# 3. Usar o operador ternário para determinar o maior de dois números fornecidos pelo usuário
nota1 = int(input())
nota2 = int(input())

maior = f'{nota1} É maior' if nota1 > nota2 else f'{nota2} É maior'
print(maior)
