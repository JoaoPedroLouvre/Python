import pprint # Módulo para ajustar a legibilidade do código

# Um dicionário dentro de outro

gamesDict = {
    'gameFifa':{
        'yearLaunch': 2022,
        'classification': 8.5,
        'genero': ['esportes', 'familia']
    },
    'mario odyssey':{
        'yearLaunch': 2017,
        'classification': 10.0,
        'genero': ['aventura', '3d']
    },
    'donkey kong country':{
        'yearLaunch': 1995,
        'classification': 9.5,
        'genero': ['aventura', 'plataforma']
    },
}

pp = pprint.PrettyPrinter(depth=4)
pp.pprint(gamesDict)


# 1 - Buscar informação dentro de um dicionario aninhado
print(gamesDict['mario odyssey']['genero'])

# 2 - Adicionar um novo item
gamesDict['mario odyssey']['players'] = 1
print(gamesDict['mario odyssey'])

# 3 - Excluir um dicionário
del gamesDict['gameFifa']
pp.pprint(gamesDict)