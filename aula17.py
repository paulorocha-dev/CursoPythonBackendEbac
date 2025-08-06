# Escreva um programa que receba três números inteiros e exiba o segundo maior número.

# 1. Preciso receber esses números separadamente.

numero1, numero2, numero3 = map(int, input().split())

# 2. Criar uma lógica para identificar o segundo maior número.

meu_array = []

meu_array.append(numero1)
meu_array.append(numero2)
meu_array.append(numero3)

meu_array.sort()

print(meu_array[1])



# 3. Exibir o segundo maior número.


