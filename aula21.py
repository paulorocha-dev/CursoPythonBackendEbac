# Soma de 1 a N: Receba um número N e exiba a soma de todos os números de 1 até N

# 1. Receber o número N

numero_n = int(input())

# 2. Exibiar a soma de todos os números de 1 até N

soma = 0

for i in range(1, numero_n + 1):
    soma += i

print(soma)