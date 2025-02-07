# 2. Determinar se um ano fornecido pelo usuário é bissexto ou não
# Lembre-se que um ano é bissexto se for divisível por 4 e, se for divisível por 100, deve ser também divisível por 400.

anoEscolhido = int(input('Escolha um ano para a verificação: ')) 
algarismos = anoEscolhido % 100
if algarismos % 4 == 0: 
    print(f'{anoEscolhido} é bissexto.')
else:
    print(f'{anoEscolhido} não é bissexto.')