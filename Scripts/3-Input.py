# Utilizando o input

# O input sempre converte o valor recebido para uma string, logo para transforma-lo em outro valor nós utilizamos
# int(), float(), bool(), etc
name = input('Digite o nome do jogo:\n  ')
yearLaunch = int(input('Digite o ano de lançamento do jogo:\n  '))
gamePrice = float(input('Digite o preço do jogo\n  '))
gamePass = bool(input('Está incluso no plano mensal?\n '))

print(name)
print(yearLaunch)
print(gamePrice)
print(gamePass)