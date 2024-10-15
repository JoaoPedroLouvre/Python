"""
*args - Utilizamos ele quando não temos certeza de quantos argumentos queremos ter em uma função
*     - Os argumentos são passados para ele como uma tupla

* **kwargs - Além dos valores podemos passar também as respectivas chaves para cada argumento
*          - Os argumentos são passados como um dicionário
"""

# 1 - Soma de números utilizando args:

def sum(*num): 
    sum_total = 0
    for n in num:
        sum_total += n
    print(f'Soma é {sum_total}')

sum(7, 9, 10, 11, 24)

# 2 - Apresentação de cursos:
def presentation(**data):
    for key, value in data.items():
        print(f'{key} - {value}')

print('###CURSO###')
presentation(name='Python', category='Backend', level='Iniciante')
presentation(name='Visão computacional com Python', category='IA', level='Avançado')
presentation(name='Dashboards com Dash', category='Data Science', level='Intermediário')