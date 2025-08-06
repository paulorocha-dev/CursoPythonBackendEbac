# Receba um número e determine se ele é um palíndromo (lê-se igual de trás para frente).

# 1. Receber um número inteiro

meu_numero = int(input("Digite um número inteiro: "))

# 2. Determinar se o número é palíndromo
# 3. Retornar a respost

minha_string = str(meu_numero)

if minha_string == minha_string[::-1]:
    print("O número é um palíndromo.")
else:
    print("O número não é um palíndromo.")
