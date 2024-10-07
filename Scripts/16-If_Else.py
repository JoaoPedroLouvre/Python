name = input('digite o nome do jogo: ')
yearLaunch = int(input('digite o ano de lançamento do jogo: '))
classification = float(input('digite a nota de classificação do jogo: '))

if classification >= 8.0 or yearLaunch > 2015:
    print(f'O jogo {name} é bom! Recomendo joga-lo!')
else:
    print(f'O jogo {name} ainda não atingiu uma boa nota. Por isso não recomendo! :(')
    