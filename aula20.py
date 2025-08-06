# Tabuada: Receba um número e exiba a sua tabuada de 1 a 10.

# 1. Receber o número

numero_tabuada = float(input())

# 2. Criar a lógica para exibir a tabuada

for i in range(1, 11):
    print(numero_tabuada * i)