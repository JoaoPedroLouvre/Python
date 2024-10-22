"""
TODO: ## Conta letras maiúsculas e minúsculas
TODO: ## Escreva uma função Python que receba uma string e conte o número de letras
TODO: ## maiúsculas e minúsculas desta string.
"""

def contadorLetras (frase):
    qtdmaiuscula = 0
    qtdminuscula = 0

    for letra in frase:
        if letra.isupper():
            qtdmaiuscula += 1
        elif letra.islower():
            qtdminuscula += 1
    
    return qtdminuscula, qtdmaiuscula

frase = input('Informe uma palavra: ')
minuscula, maiuscula = contadorLetras(frase)
print(f'Letras minúsculas: {minuscula}')
print(f'Letras maíusculas: {maiuscula}')