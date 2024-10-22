# No python slice pode ser usado também para strings e não só para arrays (como no javascript)
gameName = 'Fifa 23'
gameDescription = '''
Fifa 23 é um jogo de futebol desenvolvido pela EA Sports
e que posibilita jogar localmente ou online
'''

# string[inicio:fim] - indice começa na posição 0 | indice final -1

# 1 - Busque toda string a partir da primeira posição
print(gameName[0:])
print(gameName[1:])

# 2 - Busque toda string a partir da ultima posição
print(gameName[:7])
print(gameName[:4])

# 3 - Busque toda string da terceira até a ultima posição
print(gameName[2:])

'''
string[inicio:fim:passo] - indice começa na posição 0 | indice final -1
passo - determina o incremento. Por padrão esse número é o 1. (Intervalo)
'''

# 4 - Busque toda string de dois em dois caracteres
print(gameName[::2])

# 5 - Busque toda a string nos indices ímpares
print(gameName[1::2])

# 6 - Inverter uma string de trás para frente
print(gameName[::-1])
print(gameDescription[::-1])