num1 = int(input('Digite o primeiro número: \n'))
num2 = int(input('Digite o segundo número: \n'))

# Aritméticos
som = num1 + num2
sub = num1 - num2
div = num1 / num2
mult = num1 * num2
mod = num1 % num2
exp = num1 ** num2

print(f'Resto da divisão de {num1} por {num2} é {mod}')
print(f'Potência do número {num1} por {num2} é {exp}')

# Comparação 
bigger = num1 > num2
smaller = num1 < num2
equal = num1 == num2
diferent = num1 != num2
bigger_equal = num1 >= num2
smaller_equal = num2 <=num2

print(equal)
print(bigger_equal)

# Atribuição
# {num1 = num1 + 1} é exatamente igual a: {num1 +=1}