salario = int(input('Por favor informe o seu salário: '))

if salario > 1250:
    percentual = (10/100) * salario
    print(salario + percentual)
elif salario < 1250:
    percentual = (15/100) * salario
    print(salario + percentual)