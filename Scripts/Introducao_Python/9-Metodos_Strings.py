gameName = 'Fifa 23'
gameDescription = '''
Fifa 23 é um jogo de futebol, desenvolvido pela EA Sports,
e que posibilita jogar localmente ou online
'''

# Retornar string em maíusculo
print(gameName.upper())

# Retorna string em minúsculo
print(gameName.lower())

# Apenas primeira letra em maíusculo
print(gameName.capitalize())
print(gameName.title())

# Retorna 10 caracteres, e preenche os espaços vazios com '-'
print(gameName.center(10, '-'))

# Retorna a posição de um determinado caractere na string
print(gameName.find('a'))

# Contar caracteres
print(gameDescription.count('f'))
print(gameDescription.count('a'))

# Alterar valor dentro de uma string por outro
print(gameDescription.replace('Fifa', 'PES'))

# Quebra a string por um elemento
print(gameDescription.split(','))