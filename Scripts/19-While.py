gameName = input('Digite o nome do jogo:\n')
qtdRating = 0
totalRating = 0
rating = 0

while(rating != -1): # Diferente do for no while nós definimos uma condição de parada não precisando
                     # dizer quantas iterações vão ser feitas
    rating = float(input('Informe a nota do jogo\n'))
    if rating != -1:
        totalRating += rating
        qtdRating += 1
        average = totalRating / qtdRating
print(f'Média das avaliações do jogo {gameName} é {average:.2f}')