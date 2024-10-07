'''
1 - Substituindo caractere repetido

Escreva um programa Python para obter uma string de uma determinada string em que todas as ocorrências de seu primeiro caractere foram alteradas para '$', exceto o próprio primeiro caractere
Ex:
    fifa 23 → fi$a 23
'''

name = input('Digite um nome: \n') # Pedimos um nome qualquer ao usuario
char = name[0].lower() # Selecionamos a primeira letra do nome e deixamos ela minúscula
new_name = name.replace(char, '$') # Definimos new_name subistituindo a primeira letra de name por $
new_name = char + new_name[1:] # Dizemos que new name recebe a primeira letra em minúscula mais a substituição a partir do 2° Elemento
print(new_name)