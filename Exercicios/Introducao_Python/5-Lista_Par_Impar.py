"""
TODO: ## Lista números pares e ímpares de uma lista
TODO: ## Escreva uma função Python para imprimir os números pares e ímpares em duas listas 
TODO: ## separadas para cada uma.
"""
def separadorNumeros(numeros):
    par = []
    impar = []

    for num in numeros:
        if num % 2 == 0:
            par.append(num)
        elif num % 2 == 1:
            impar.append(num)
    
    return par, impar

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares, impares = separadorNumeros(numeros)
print(f'Números pares da lista: {pares}')
print(f'Números ímpares da lista: {impares}')