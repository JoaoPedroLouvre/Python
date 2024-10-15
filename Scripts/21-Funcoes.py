# 1 - Função para imprimir hello world
def wellcome():
    print('Hello World')

wellcome()

# 2 - FUnção para somar dois números
def sum(a, b):
    print(a + b)

num1 = int(input('Informe o 1° número: '))
num2 = int(input('Informe o 2° número: '))
sum(num1, num2)

# 3 - Função para cadastrar o jogo

def create_game():
    name = input('Digite o nome do jogo: \n  ')
    yearLaunch = int(input('Digite o ano de lançamento do jogo: \n  '))
    gamePrice = float(input('Digite o preço do jogo: \n  '))
    noteRating = float(input('Digite a nota de avaliação do jogo: \n '))

    print(f'{name} - R$ {gamePrice}')

create_game()