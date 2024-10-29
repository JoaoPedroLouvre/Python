# 1 - Liste valores de 0 a 10 que sejam menor que 4
for i in range(10):
    if i < 4:
        print(i)


# Desenvolvendo o mesmo programa de cima utilizando list_comprehesion
listNumbers = [i for i in range(10) if i < 4] # Retorna o valor em uma lista
print(listNumbers)

gamesList = ['Mario Odyssey', 'DK Country', 'Luigis Mansion', 'Kirby']

# 2 - Jogos que possuam a letra A utilizando list_comprehesion
newList = [x for x in gamesList if 'a' in x]
print(newList)

# 3 - Jogos que eu zerei
gamesFinished = [x for x in gamesList if x != 'Kirby']
print(gamesFinished)

# 3 - Jogos que eu zerei ( mais refinado )
print(f'Lista de jogos \n {gamesList}')
nZerado = input('Informe o jogo da lista que você não zerou: ')
gamesFinishedRefined = [x for x in gamesList if x != nZerado]
print(gamesFinishedRefined)