import statistics


# * 1 - Aplicar a média
print(statistics.mean([3, 2, 5, 8, 7]))

# * 2 - Aplicar a mediana
print(statistics.median([1, 2, 3, 4, 5]))

# * 3 - Aplicar a moda
print(statistics.mode([1, 2, 3, 1, 23, 5, 1, 2]))

# * 4 - Devio padrão 
"""
- Quanto mais próximo de 0 for o desvio padrão, significa que os dados do conjunto estão menos dispersos
"""
print(statistics.stdev([1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5]))