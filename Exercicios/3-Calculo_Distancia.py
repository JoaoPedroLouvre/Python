distancia = int(input('Por favor, informe a distancia que você deseja percorrer em km: '))

if distancia <= 200:
    passagem = 0.50
    print(distancia * passagem)
else:
    passagem = 0.35
    print(distancia * passagem)