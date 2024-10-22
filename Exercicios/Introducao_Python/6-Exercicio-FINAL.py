times = {}

done = False

# 1 - Listar Times
def listar_times():
    if times:
        print('Times Listados: ')
        for i, time in enumerate(times.values()):
            print(f'{i+1}. {time["name"]} ({len(time["jogadores"])} jogadores)')
    else:
        print('Nenhum time cadastrado!')

# 2 - Adicionar Time
def adicionar_times():
    time_nome = input('Digite o nome do time:\n')
    if time_nome not in times:
        times[time_nome] = {'name': time_nome, 'jogadores': []}
        print('Time adicionado!')
    else:
        print('Time já existe!')

# 3 - Remover Time
def remover_time():
    if times:
        listar_times()
        time_num = int(input('Informe o número do time que deseja remover: '))
        if 1 <= time_num <= len(times):
            time_nome = list(times.keys())[time_num - 1]
            del times[time_nome]
            print('Time removido!')
        else:
            print('Número inválido!')
    else:
        print('Nenhum time cadastrado!')

# 4 - Adicionar jogador a um time
def adicionar_jogador():
    if times:
        listar_times()
        time_num = int(input('Informe o número do time que deseja adicionar o jogador:\n'))
        if 1 <= time_num <= len(times):
            time_nome = list(times.keys())[time_num - 1]
            jogador_nome = input('Informe o nome do jogador:\n')
            times[time_nome]['jogadores'].append(jogador_nome)
            print('Jogador adicionado no time!')
        else:
            print('Número do time inválido!')
    else:
        print('Nenhum time cadastrado!')

# 5 - Remover jogador de um time
def remover_jogador():
    if times:
        listar_times()
        time_num = int(input('Informe o número do time que deseja remover o jogador:\n'))
        if 1 <= time_num <= len(times):
            time_nome = list(times.keys())[time_num - 1]
            jogadores = times[time_nome]['jogadores']
            if jogadores:
                for i, jogador in enumerate(jogadores):
                    print(f'{i+1}. {jogador}')
                jogador_num = int(input('Informe o número do jogador que deseja remover:\n'))
                if 1 <= jogador_num <= len(jogadores):
                    del jogadores[jogador_num - 1]
                    print('Jogador removido do time!')
                else:
                    print('Número do jogador inválido!')
            else:
                print('Esse time não tem jogadores!')
        else:
            print('Número do time inválido!')
    else:
        print('Nenhum time cadastrado!')

# 6 - Listar Jogadores de um time
def listar_jogadores():
    if times:
        listar_times()
        time_num = int(input('Informe o número do time que deseja listar os jogadores:\n'))
        if 1 <= time_num <= len(times):
            time_nome = list(times.keys())[time_num - 1]
            jogadores = times[time_nome]['jogadores']
            if jogadores:
                print(f'Jogadores do time {time_nome}:')
                for i, jogador in enumerate(jogadores):
                    print(f'{i+1}. {jogador}')
            else:
                print(f'O time {time_nome} não tem jogadores.')
        else:
            print('Número do time inválido!')
    else:
        print('Nenhum time cadastrado!')

while not done:
    # Opções do programa
    print('********************************')
    print('Selecione uma das opções abaixo:')
    print('1) Listar Times')
    print('2) Adicionar Time')
    print('3) Remover Time')
    print('4) Adicionar Jogador')
    print('5) Remover Jogador')
    print('6) Listar Jogadores')
    print('7) Sair')
    print('********************************')

    choice = input('>')
    if choice == '1':
        listar_times()
    elif choice == '2':
        adicionar_times()
    elif choice == '3':
        remover_time()
    elif choice == '4':
        adicionar_jogador()
    elif choice == '5':
        remover_jogador()
    elif choice == '6':
        listar_jogadores()
    elif choice == '7':
        done = True
    else:
        print('Opção Inválida')