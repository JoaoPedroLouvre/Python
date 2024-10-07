gameList = ['Fifa', 'God od War', 'Red Dead 2', 'Uncharted'] # Funciona inclusive com outros valores, números e etc

# 1 - Iterando valores de uma lista (Percorre todos os valores da lista)
for game in gameList:
    print(game)

# 2 - Quando a condição for atendida, o loop será encerrado
for game in gameList:
    if game == 'Red Dead 2':
        break # Para a iteração quuando chegar a red dead 2 nem chegando a imprimir este método
    print(game)
print('\n')

# 3 - Quando a condição for atendida, o loop vai para próxima iteração
for game in gameList:
    if game == 'Red Dead 2':
        continue # Quando entrar na condição ele pula para próxima iteração
    print(game)

# 4 - Avaliação do Jogo
gameName = input('Digite o nome do jogo\n')
gameRating = int(input('Digite quantas avaliações deseja fazer no jogo\n'))

sum = 0
for i in range(gameRating): # Define um valor limite. De 0 até o valor entre parênteses ele executa
    note = float(input('Digite a nota para o jogo\n'))
    sum += note
print(f'Média de avaliação do jogo {gameName} é {sum/gameRating:.2f}')