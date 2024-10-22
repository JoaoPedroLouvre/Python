'''
Troca de caracteres:

2 - Escreva um programa Python para obter uma única string de duas strings forne
separadas por um espaço e troque os dois primeiros caracteres de cada string.

Ex: abc xyz -> xyc abz
'''

str1 = 'abc' 
str2 = 'xyz'

new_str1 = str2[:2] + str1[2:] # Recebe o primeiro e 2 elemento do str2 e do segundo caractere em diante do str1 ou seja, xy + c
new_str2 = str1[:2] + str2[2:]
print(new_str1, '+', new_str2)