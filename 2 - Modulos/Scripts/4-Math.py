import math

# * 1 - Acessar o número PI
print(math.pi)
print(f'{math.pi:.2f}') 

# * 2 - Acessar o número de Euler
print(math.e)
print(f'{math.e:.2f}')

# * 3 - Arredondar número para cima ou para baixo
num = 10.4
print(math.ceil(num))
print(math.floor(num))

# * 4 - Fatorial de um número
num1 = 7
print(math.factorial(num1))

# * 5 - Potência de números
print(math.pow(2,2))

# * 6 - Raiz quadrada de um número
print(math.sqrt(169))

# * 7 - MDC
mdc = math.gcd(25, 100) # 25 / 100
print(mdc)

# * 8 - Logaritmo
print(math.log(10))