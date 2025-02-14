# Escreva uma função que conta a quantidade de vogais em um texto e armazena tal
# quantidade em um dicionário, onde a chave é a vogal considerada e o valor é a quantidade
# de vezes que essa vogal aparece no texto.
# A função deve receber o texto como entrada e retornar o dicionário.

def vogal(frase):
    numero_a = 0
    numero_e = 0
    numero_i = 0
    numero_o = 0
    numero_u = 0
    for letra in frase:
        if letra == 'a':
            numero_a += 1
        if letra == 'e':
            numero_e += 1
        if letra == 'i':
            numero_i += 1
        if letra == 'o':
            numero_o += 1
        if letra == 'u':
            numero_u += 1
    
    return {'a' : numero_a, 'e' : numero_e, 'i' : numero_i, 'o' : numero_o, 'u' : numero_u}

print(vogal('Faculdade Impacta'))


